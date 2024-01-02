import discord
import responses
from discord.ext import tasks, commands
from dicecog import DiceCog
from calculator import CalculatorCog
import requests as re

master_list = []

def run_discord_bot():
    TOKEN = 'REDACTED'
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        # my_task.start()
        await bot.add_cog(DiceCog(bot))
        await bot.add_cog(CalculatorCog(bot))
        print(f'{bot.user} is now running!')

    @bot.command()
    async def ping(ctx):
        await ctx.send(responses.handle_response("ping"))

    @bot.command()
    async def hello(ctx):
        await ctx.send(responses.handle_response("hello"))

    @bot.command(aliases=['8ball'])
    async def eight_ball(ctx, *args):
        if len(args) <= 0:
            c = "Please ask a question"
            await ctx.send(c)
        else:
            await ctx.send(responses.handle_response("8ball"))

    @bot.command()
    async def trivia(ctx, *args):
        trivia_api_url = 'REDACTED'

        response = re.get(trivia_api_url)
        data = response.json()

        if data["response_code"] != 0:
            x = "ERROR: cannot fetch trivia question (not my fault)"
            await ctx.send(x)
        else:
            x = data["results"][0]["question"]
            y = data["results"][0]["correct_answer"]
            await ctx.send(str(x) + " " + str(y))

    @bot.command(aliases=['rockpaperscissors'])
    async def rps(ctx, arg=None):
        if not arg:
            c = "Please enter a valid rock-paper-scissors value."
            await ctx.send(c)
            return
        x = arg.lower()
        ans = ["rock", "paper", "scissors"]
        c = "you should not see this value"
        if (x != "rock") and (x != "paper") and (x != "scissors"):
            c = "Please enter a valid rock-paper-scissors value."
        else:
            val = ans[responses.handle_response("rps")]
            if (x == ans[0] and val == ans[1]) or (x == ans[1] and val == ans[2]) or (x == ans[2] and val == ans[0]):
                c = f"You lose! I got {val}."
            else:
                c = f"You win! I got {val}."
        await ctx.send(c)

    @bot.command()
    async def database(ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            command = args[0]
            if command == "add":
                if ' '.join(args[1:]) in master_list:
                    x = f"{' '.join(args[1:])} already in database, not added."
                else:
                    master_list.append(' '.join(args[1:]))
                    x = f"{' '.join(args[1:])} added to database!"
            elif command == "show":
                if master_list:
                    x = ', '.join(master_list)
                else:
                    x = "Database is empty."
            elif command == "remove" or command == "delete":
                if ' '.join(args[1:]) in master_list:
                    master_list.remove(' '.join(args[1:]))
                    x = f"{' '.join(args[1:])} removed from database!"
                else:
                    x = f"{' '.join(args[1:])} not in database."
            elif command == "clear":
                x = "Are you sure you wish to clear the database? Y/N"
                await ctx.send(x)
                response = await bot.wait_for("message", timeout=10) # TODO: FIX THIS

                if response.content.lower() == "y" or response.content.lower() == "yes":
                    master_list.clear()
                    x = "Database cleared :("
                elif response.content.lower() == "n" or response.content.lower() == "no":
                    x = "Database not cleared."
                else:
                    x = "Invalid response, aborting."
            await ctx.send(x)

    bot.run(TOKEN)
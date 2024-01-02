import discord
import responses
from discord.ext import tasks, commands

master_list = []

def run_discord_bot():
    TOKEN = 'REDACTED FOR SECURITY REASONS'
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
        # my_task.start()
        print(f'{bot.user} is now running!')

    @bot.command()
    async def test(ctx):
        await ctx.send(responses.handle_response("ping"))

    @bot.command()
    async def hello(ctx):
        await ctx.send(responses.handle_response("hello"))

    @bot.command()
    async def d4(ctx):
        await ctx.send(responses.handle_response("d4"))

    @bot.command()
    async def d6(ctx):
        await ctx.send(responses.handle_response("d6"))

    @bot.command()
    async def d8(ctx):
        await ctx.send(responses.handle_response("d8"))

    @bot.command()
    async def d10(ctx):
        await ctx.send(responses.handle_response("d10"))

    @bot.command()
    async def d12(ctx):
        await ctx.send(responses.handle_response("d12"))

    @bot.command()
    async def d20(ctx):
        await ctx.send(responses.handle_response("d20"))

    @bot.command()
    async def d100(ctx):
        await ctx.send(responses.handle_response("d100"))

    @bot.command()
    async def coin(ctx):
        await ctx.send(responses.handle_response("coin"))

    @bot.command()
    async def rps(ctx, arg):
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
    async def add(ctx, *args):
        x = 0
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            for i in args:
                x += int(i)
            await ctx.send(x)

    @bot.command()
    async def subtract(ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            x = int(args[0])
            l = args[1:]
            for i in l:
                x -= int(i)
            await ctx.send(x)

    @bot.command()
    async def multiply(ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            x = int(args[0])
            l = args[1:]
            for i in l:
                x *= int(i)
            await ctx.send(x)

    @bot.command()
    async def divide(ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            x = int(args[0])
            l = args[1:]
            if "0" in l:
                x = "ERROR: cannot divide by 0"
                await ctx.send(x)
            else:
                for i in l:
                    x /= int(i)
                await ctx.send("{:.5f}".format(x))

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
                else:
                    x = "Database not cleared."
            await ctx.send(x)

    bot.run(TOKEN)
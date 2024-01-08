import discord
import responses
from discord.ext import tasks, commands
from dicecog import DiceCog
from calculator import CalculatorCog
import requests as re
import html
import datetime

master_list = []
activePing = 0

def run_discord_bot():
    TOKEN = 'REDACTED'
    bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

    @bot.event
    async def on_ready():
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
        def check(message):
            return message.channel == ctx.channel and message.author != bot.user
        trivia_api_url = 'https://opentdb.com/api.php?amount=1'

        response = re.get(trivia_api_url)
        data = response.json()

        if data["response_code"] != 0:
            x = "ERROR: cannot fetch trivia question (not my fault)"
            await ctx.send(x)
        else:
            if data["results"][0]["type"] == "boolean":
                question = html.unescape(data["results"][0]["question"])
                answers = "\nA: True\nB: False"
                await ctx.send(question + answers)

                while True:
                    try:
                        response = await bot.wait_for("message", check=check, timeout=10)

                        if (response.content.lower() == "a" or response.content.lower() == "true") and data['results'][0]['correct_answer'] == 'true':
                            x = f"{response.author} is correct! It is true."
                            await ctx.send(x)
                            break
                        elif (response.content.lower() == "b" or response.content.lower() == "false") and data['results'][0]['correct_answer'] == 'false':
                            x = f"{response.author} is correct! It is false."
                            await ctx.send(x)
                            break
                        elif (response.content.lower() == "a" or response.content.lower() == "true") and data['results'][0]['correct_answer'] == 'false':
                            x = f"{response.author} is wrong! It is false."
                            await ctx.send(x)
                            break
                        elif (response.content.lower() == "b" or response.content.lower() == "false") and data['results'][0]['correct_answer'] == 'true':
                            x = f"{response.author} is wrong! It is true."
                            await ctx.send(x)
                            break
                    except:
                        x = f"Time's up! The correct answer is {data['results'][0]['correct_answer']}."
                        await ctx.send(x)
                        break
            
            else:
                ans = {
                    1: data["results"][0]["correct_answer"],
                    2: data["results"][0]["incorrect_answers"][0],
                    3: data["results"][0]["incorrect_answers"][1],
                    4: data["results"][0]["incorrect_answers"][2],
                }
                indx = responses.handle_response("trivia")
                question = html.unescape(data["results"][0]["question"])
                answers = f"\nA: {ans[indx[0]]}\nB: {ans[indx[1]]}\nC: {ans[indx[2]]}\nD: {ans[indx[3]]}"
                await ctx.send(question + answers)

                while True:
                    try:
                        response = await bot.wait_for("message", check=check, timeout=10)

                        if response.content.lower() == "a" and data['results'][0]['correct_answer'] == ans[indx[0]]:
                            x = f"{response.author} is correct! It is {data['results'][0]['correct_answer']}."
                            await ctx.send(x)
                            break
                        elif response.content.lower() == "b" and data['results'][0]['correct_answer'] == ans[indx[1]]:
                            x = f"{response.author} is correct! It is {data['results'][0]['correct_answer']}."
                            await ctx.send(x)
                            break
                        elif response.content.lower() == "c" and data['results'][0]['correct_answer'] == ans[indx[2]]:
                            x = f"{response.author} is correct! It is {data['results'][0]['correct_answer']}."
                            await ctx.send(x)
                            break
                        elif response.content.lower() == "d" and data['results'][0]['correct_answer'] == ans[indx[3]]:
                            x = f"{response.author} is correct! It is {data['results'][0]['correct_answer']}."
                            await ctx.send(x)
                            break
                        elif (response.content.lower() == "a" and data['results'][0]['correct_answer'] != ans[indx[0]]) or (response.content.lower() == "b" and data['results'][0]['correct_answer'] != ans[indx[1]]) or (response.content.lower() == "c" and data['results'][0]['correct_answer'] != ans[indx[2]]) or (response.content.lower() == "d" and data['results'][0]['correct_answer'] != ans[indx[3]]):
                            x = f"{response.author} is incorrect! The correct answer is {data['results'][0]['correct_answer']}."
                            await ctx.send(x)
                            break
                    except:
                        x = f"Time's up! The correct answer is {data['results'][0]['correct_answer']}."
                        await ctx.send(x)
                        break

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
            elif (x == val):
                c = f"Tie! I got {val}."
            else:
                c = f"You win! I got {val}."
        await ctx.send(c)

    @bot.command(aliases=['db'])
    async def database(ctx, *args):
        def check(message):
            return message.channel == ctx.channel and message.author == ctx.author and message.author != bot.user
        
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

                while True:
                    try:
                        response = await bot.wait_for("message", check=check, timeout=10)

                        if response.content.lower() == "y" or response.content.lower() == "yes":
                            master_list.clear()
                            x = "Database cleared :("
                            break
                        elif response.content.lower() == "n" or response.content.lower() == "no":
                            x = "Database not cleared."
                            break
                    except:
                        x = "No valid response, aborting."
                        break
            
            await ctx.send(x)

    @bot.command()
    async def joke(ctx, arg=None):
        if arg == 'nsfw':
            joke_api_url = 'https://v2.jokeapi.dev/joke/Any'
            response = re.get(joke_api_url)
            data = response.json()

            if data["type"] == "twopart":
                joke = data["setup"] + " " + data["delivery"]
            else:
                joke = data["joke"]
            await ctx.send(joke)
        else:
            joke_api_url = 'https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit'
            response = re.get(joke_api_url)
            data = response.json()

            if data["type"] == "twopart":
                joke = data["setup"] + " " + data["delivery"]
            else:
                joke = data["joke"]
            await ctx.send(joke)


    @bot.command()
    async def cat(ctx):
        cat_api_url = 'https://api.thecatapi.com/v1/images/search'
        response = re.get(cat_api_url)
        data = response.json()

        img = data[0]["url"]

        await ctx.send(img)

    @bot.command()
    async def dog(ctx):
        cat_api_url = 'https://dog.ceo/api/breeds/image/random'
        response = re.get(cat_api_url)
        data = response.json()

        img = data["message"]

        await ctx.send(img)

    @bot.command(aliases=['kanyewest'])
    async def kanye(ctx):
        cat_api_url = 'https://api.kanye.rest/'
        response = re.get(cat_api_url)
        data = response.json()

        img = data["quote"] + " -Kanye West"

        await ctx.send(img)

    @bot.command(aliases=['task', 'bored'])
    async def activity(ctx):
        task_api = 'https://www.boredapi.com/api/activity/'
        response = re.get(task_api)
        data = response.json()

        img = data["activity"]

        await ctx.send(img)

    @bot.command(aliases=['chuck', 'norris'])
    async def chucknorris(ctx):
        chuck_api = 'https://api.chucknorris.io/jokes/random'
        response = re.get(chuck_api)
        data = response.json()

        joke = data["value"]
        await ctx.send(joke)

    @bot.command(aliases=['guess', 'guessnum', 'guessthenum'])
    async def guessthenumber(ctx):
        def check(message):
            return message.channel == ctx.channel and message.author != bot.user

        val = responses.handle_response("guess")
        c = "Guess the number between 1 and 100!"
        await ctx.send(c)

        while True:
            try:
                response = await bot.wait_for("message", check=check, timeout=5)
                if int(response.content) == int(val):
                    c = f"{response.author} got it! The number is {val}."
                    await ctx.send(c)
                    break
                elif response.content.isnumeric() and int(response.content) != int(val):
                    c = f"{response.author} is wrong! The number is {val}."
                    await ctx.send(c)
                    break
            except:
                c = f"Time's up! The number is {val}."
                await ctx.send(c)
                break

    @bot.command()
    async def activatepings(ctx):
        global activePing

        if activePing == 0:
            my_task.start()
            activePing = 1
            c = f"Pings enabled! {activePing}"
            await ctx.send(c)
        else:
            my_task.stop()
            activePing = 0
            c = f"Pings disabled! {activePing}"
            await ctx.send(c)

    @tasks.loop(seconds=60) # FILL IN
    async def my_task():
        d = datetime.datetime.now()
        channel_id = 'TODO'
        channel = bot.get_channel(channel_id)

        if d.minute == 49:
            await channel.send("<@&ROLE_ID> TIME TO ROLL!")

    bot.run(TOKEN)
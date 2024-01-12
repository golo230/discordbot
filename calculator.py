import discord
from discord.ext import commands
import math

class Calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def add(self, ctx, *args):
        x = 0
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                for i in args:
                    x += float(i)
                await ctx.send("{:.3f}".format(x))
            except Exception as e:
                x = "INVALID PARAMETER: " + str(e)
                await ctx.send(x)

    @commands.command()
    async def subtract(self, ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = float(args[0])
                l = args[1:]
                for i in l:
                    x -= float(i)
                await ctx.send("{:.3f}".format(x))
            except Exception as e:
                x = "INVALID PARAMETER: " + str(e)
                await ctx.send(x)

    @commands.command()
    async def multiply(self, ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = float(args[0])
                l = args[1:]
                for i in l:
                    x *= float(i)
                await ctx.send("{:.3f}".format(x))
            except Exception as e:
                x = "INVALID PARAMETER: " + str(e)
                await ctx.send(x)

    @commands.command()
    async def divide(self, ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = float(args[0])
                l = args[1:]
                for i in l:
                    x /= float(i)
                await ctx.send("{:.3f}".format(x))
            except Exception as e:
                x = "INVALID PARAMETER: " + str(e)
                await ctx.send(x)

    @commands.command()
    async def mod(self, ctx, *args):
        if len(args) <= 0:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = int(args[0])
                l = args[1:]
                for i in l:
                    x %= int(i)
                await ctx.send(x)
            except Exception as e:
                x = "INVALID PARAMETER: " + str(e)
                await ctx.send(x)

    @commands.command()
    async def sin(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.sin(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command()
    async def cos(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.cos(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command()
    async def tan(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.tan(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command()
    async def sqrt(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.sqrt(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command(aliases=['ln'])
    async def log(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.log(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command()
    async def log10(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.log10(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command()
    async def log2(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.log2(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)

    @commands.command()
    async def exp(self, ctx, arg=None):
        if not arg:
            x = "no parameters provided"
            await ctx.send(x)
        else:
            try:
                x = math.exp(float(arg))
                await ctx.send("{:.5f}".format(x))
            except Exception as e:
                    x = "INVALID PARAMETER: " + str(e)
                    await ctx.send(x)
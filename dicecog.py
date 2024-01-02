import discord
import responses
from discord.ext import commands

class DiceCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def d4(self, ctx):
        await ctx.send(responses.handle_response("d4"))

    @commands.command()
    async def d6(self, ctx):
        await ctx.send(responses.handle_response("d6"))

    @commands.command()
    async def d8(self, ctx):
        await ctx.send(responses.handle_response("d8"))

    @commands.command()
    async def d10(self, ctx):
        await ctx.send(responses.handle_response("d10"))

    @commands.command()
    async def d12(self, ctx):
        await ctx.send(responses.handle_response("d12"))

    @commands.command()
    async def d20(self, ctx):
        await ctx.send(responses.handle_response("d20"))

    @commands.command()
    async def d100(self, ctx):
        await ctx.send(responses.handle_response("d100"))

    @commands.command()
    async def coin(self, ctx):
        await ctx.send(responses.handle_response("coin"))
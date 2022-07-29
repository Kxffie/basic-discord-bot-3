from nextcord.ext import commands
import nextcord


class Basic(commands.Cog):
    def __init__(self, client):
        super().__init__()

    @commands.command()
    async def hello(self, ctx):
        await ctx.send(f'Hello {ctx.author.mention}!')


def setup(client):
    client.add_cog(Basic(client))

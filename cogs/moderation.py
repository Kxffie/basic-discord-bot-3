from nextcord.ext import commands
import nextcord

from config import config


class Moderation(commands.Cog):
    def __init__(self, client):
        super().__init__()
        self.client = client

    # @commands.command()
    # async def hello(self, ctx):
    #     await ctx.send(f'Hello {ctx.author.mention}!')
    
    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = nextcord.Embed(title=f'{member} has joined!', description=f'Welcome!', color=0x00ff00)
        Achannel = self.client.get_channel(config.alertsChannel)
        Wchannel = self.client.get_channel(config.welcomeChannel)
        await Achannel.send(embed=embed)
        await Wchannel.send(embed=embed)
        
    @commands.Cog.listener()
    async def on_member_remove(self, member):
        embed = nextcord.Embed(title=f'{member} has left', description=f'Sad to see you go', color=0x00ff00)
        Achannel = self.client.get_channel(config.alertsChannel)
        Wchannel = self.client.get_channel(config.welcomeChannel)
        await Achannel.send(embed=embed)
        await Wchannel.send(embed=embed)
    
#! --------------------------------------------------

    @commands.command()
    @commands.has_role("Admin")
    async def kick(self, ctx, member: nextcord.Member, *, reason=None):
        invite = await ctx.channel.create_invite(max_age=0, max_uses=1, unique=True)
        
        embed = nextcord.Embed(title="Kicked Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Kicked by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon, url=invite.url)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        await member.send(embed=embed)
        
        await member.kick(reason=reason)
        channel = self.client.get_channel(config.alertsChannel)
        await channel.send(embed=embed)
        
    @commands.command()
    @commands.has_role("Admin")
    async def ban(self, ctx, member: nextcord.Member, *, reason=None):
        invite = await ctx.channel.create_invite(max_age=0, max_uses=1, unique=True)
        
        embed = nextcord.Embed(title="Banned Player", color=nextcord.Color.red())
        embed.add_field(name="Player", value=member.mention, inline=False)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_footer(text=f"Banned by {ctx.author}")
        embed.set_author(name=ctx.guild.name, icon_url=ctx.guild.icon, url=invite.url)
        embed.set_thumbnail(url=member.avatar)
        await ctx.send(embed=embed)
        await member.send(embed=embed)
        
        await member.ban(reason=reason)
        channel = self.client.get_channel(config.alertsChannel)
        await channel.send(embed=embed)
        

def setup(client):
    client.add_cog(Moderation(client))

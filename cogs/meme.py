from nextcord.ext import commands
import nextcord, urllib, json


class Meme(commands.Cog):
    def __init__(self, client):
        super().__init__()

    @commands.command()
    async def meme(self, ctx, arg=None):
        invite = await ctx.channel.create_invite(max_age=0, max_uses=0, unique=False)
        
        if arg == "help":
            embed = nextcord.Embed(title="Meme Command Help", color=0x00ff00)
            embed.set_author(name=ctx.guild.name, url=invite, icon_url=ctx.guild.icon)
            embed.add_field(name="Memes", value="`memes`", inline=False)
            embed.add_field(name="Dank Memes", value="`dankmemes`", inline=False)
            embed.add_field(name="Me IRL", value="`me_irl`", inline=False)
            embed.set_footer(text="Usage: s!meme (option)")
            await ctx.send(embed=embed)
        
        elif arg != "help":
            if arg == None:
                api = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme/")
            else:
                api = urllib.request.urlopen(f"https://meme-api.herokuapp.com/gimme/{arg}")
                
            data = json.load(api)
            
            url = data["url"]
            name = data["title"]
            author = data["author"]
            sub = data["subreddit"]
            link = data["postLink"]
            
            embed = nextcord.Embed(title=name, color=0x00ff00)
            embed.set_author(name=ctx.guild.name, url=invite, icon_url=ctx.guild.icon)
            embed.set_image(url=url)
            embed.set_footer(text=f"Poster: {author} | Sub: {sub} | Link: {link}")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Meme(client))

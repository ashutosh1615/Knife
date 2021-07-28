import discord
from discord.ext import commands
from discord.utils import get
class auto_task(commands.Cog):

    def __init__(self, bot : commands.bot):
        self.bot= bot

    @commands.command()
    async def ping(self, ctx: commands.Context):
        embed_var = discord.Embed(title = 'Ping',description= f"pong! {round(self.bot.latency*1000)}ms",color = discord.Color.random())
        await ctx.send(embed=embed_var)  

    @commands.command(pass_context=True)
    async def verify(self,ctx):
        cmdChannel = self.bot.get_channel(869894407497867334)
        if ctx.channel == cmdChannel:
            user=ctx.message.author
            role = get(user.guild.roles, name='knife members')
            if '🔪' in ctx.author.name:
                    await user.add_roles(role)
                    await discord.DMChannel.send(user,'You have been verified to the server check <#868741442695204875> and choose a division')

            else:
                await ctx.send('You dont have knife in your name add \🔪 in your username and try again')
    @commands.is_owner()
    @commands.command()
    async def say(self,ctx,user : discord.Member=None,*,message=None):
        await discord.DMChannel.send(user,message)            
                    




def setup(bot: commands.Bot):
    bot.add_cog(auto_task(bot))
from discord.ext import commands
from cogs.cog_ext import *
from cogs.concatenate import *
from cogs.modify import *
class start(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
       print("ready!")


async def setup(bot):
    bot.status = discord.Status.do_not_disturb
    await bot.load_extension('cogs.cog_ext')
    await bot.add_cog(start(bot))
    await bot.load_extension('cogs.concatenate')
    await bot.load_extension('cogs.modify')

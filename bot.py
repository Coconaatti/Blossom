import discord
from discord.ext import commands # importing fixed. (sort of)
from settings import TOKEN
from typing import Literal, Optional

# ~> configuring the bot INTENTS, STATUS and PREFIX <~
intents = discord.Intents.default()

intents.message_content = True
#bot = commands.Bot(command_prefix="!", intents=intents)
#bot.status = discord.Status.do_not_disturb

class bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents
        )
    # ~> loading FUNCTIONS, UTILITIES and COGS before starting the bot <~
    async def setup_hook(self):
            self.add_command(sync)
            await self.load_extension("cogs.setup")


@bot().command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass
        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

bot().run(TOKEN)

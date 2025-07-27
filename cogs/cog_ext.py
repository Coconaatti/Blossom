import discord  # was previously loading JSON
from discord.ext import commands
from extras.utils.sql import *


embs = {}
fetched_data = {}

# *sigh,,*  why just load the same thing twice?
# with open("extras/commands.json", mode="r", encoding="utf-8") as read_file:
#    dataj = json.load(read_file)
def loading():
    for key,val in zip(data.keys(),data):
        emb = discord.Embed(title=str(key),description=data[key]['desc'],colour=data[key]['color'])
        cur.execute(f'SELECT Commands,Content FROM {val}')
        fetched_data.update(dict(cur.fetchall()))
        cur.execute(f'SELECT Commands,Content FROM {val}')
        fetched_data2 = dict(cur.fetchall())
        for x in fetched_data2:
            emb.add_field(name=f"``{x}``",value="\u200B")
        embs[str(key)] = emb

loading()
# updating the embed footer & page increments/numbers
def update_embed(index,arg,interaction,embed):
    embs[embed].set_footer(text=f"page {index}/{len(keys) - 1}")
    return interaction.response.edit_message(embed=embs[arg])



class Pages(discord.ui.View):
    def __init__(self,arg,index):
            super().__init__()
            self.arg = arg
            self.index = index


    # FIRST
    @discord.ui.button(label="<<", style=discord.ButtonStyle.blurple)
    async def first_page(self,interaction: discord.Interaction, button: discord.ui.Button):

        self.index = 1
        self.arg = keys[self.index]
        emb = keys[self.index]
        print("FIRST:",self.index, keys) # Debugging
        await update_embed(self.index,self.arg,interaction,emb)

    # GO BACK
    @discord.ui.button(label="<", style=discord.ButtonStyle.grey)
    async def prev_page(self,interaction: discord.Interaction, button: discord.ui.Button):

        if self.index == 1:
            self.index = 9
        self.index = self.index - 1
        emb = keys[self.index]
        self.arg = keys[self.index]
        print("GO BACK:",self.index, keys) # Debugging
        await update_embed(self.index,self.arg,interaction,emb)

    # NEXT
    @discord.ui.button(label=">", style=discord.ButtonStyle.grey)
    async def next_page(self,interaction: discord.Interaction, button: discord.ui.Button):

        if self.index >= len(keys) - 1:
            self.index = 0
        self.index = self.index + 1
        emb = keys[self.index]
        self.arg = keys[self.index]
        print("NEXT:",self.index, keys) # Debugging
        await update_embed(self.index,self.arg,interaction,emb)


    # LAST
    @discord.ui.button(label=">>", style=discord.ButtonStyle.blurple)
    async def last_page(self,interaction: discord.Interaction, button: discord.ui.Button):

        self.index = len(keys) - 1
        self.arg = keys[self.index]
        emb = keys[self.index]
        print("LAST:",self.index, keys) # Debugging
        await update_embed(self.index,self.arg,interaction,emb)


class command(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx, arg):
            self.bot.case_insensitive = True
            await ctx.send("Hey :3")

    @commands.command()
    async def user(self, ctx):
        self.bot.case_insensitive = True
        for user in self.bot.users:
            await ctx.send(f"I see {len(self.bot.users)} user/s,{user.name}")


    @commands.command()
    async def ls(self,ctx, arg):
        page_btn = Pages(arg,index=keys.index(arg))
        embs[arg].set_footer(text=f"page {page_btn.index}/{len(keys) - 1}")
        await ctx.send(embed=embs[arg], view=page_btn)


    @ls.error
    async def ls_error(self,ctx,error):
        if isinstance(error, commands.MissingRequiredArgument):
                arg = keys[1]
                page_btn = Pages(arg,1)
                emb = keys[1]
                embs[emb].set_footer(text=f"page {keys.index(arg)}/{len(keys) - 1}")
                await ctx.send(embed=embs[arg], view=page_btn)

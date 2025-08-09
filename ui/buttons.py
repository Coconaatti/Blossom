## OBSOLETE. until I find a solution to my problem

import discord
from cogs.cog_ext import *

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
        embs[emb].set_footer(text=f"page {self.index}/{len(keys) - 1}")
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

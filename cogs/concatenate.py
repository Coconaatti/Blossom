from typing import List
import discord
from discord import app_commands
from discord.ext import commands
from extras.utils.sql import *
from extras.utils.fzf import *
from difflib import SequenceMatcher


class cat(commands.Cog):
    def __init__(self,bot):
        self.bot = bot


    @commands.command()
    async def cat(self,ctx,table,*reqs):
        for req in reqs:
            ''' executing an SQLite command that shows up the command next to it its content in one column.
                And then wrap it in a tuple'''
            val: List[str] = showup(table,req)
            await ctx.send(f'{val[1]}: {val[0]}')

    @cat.error
    async def cat_error(self,ctx,error):
        if isinstance(error, commands.CommandInvokeError):
            for table in tables():
                diff = SequenceMatcher(None,ctx.args[2],table[0]).ratio() * 100
                if 70 < diff < 100:
                    await ctx.send(f"***Did you mean: __{table[0]}__***")
                    val: List[str] = showup(table[0],ctx.args[3])
                    await ctx.send(f'{val[1]}: {val[0]}')
    #async def rps_autocomplete(self, interaction: discord.Interaction, current: str) -> List[app_commands.Choice[str]]:
    #    global table
    #    choices = showup(table,None)[:25]
    #    choices = [app_commands.Choice(name=choice, value=choice) for choice in choices if current.lower() in choice.lower()][:25]
    #    return choices
    #global table

    @app_commands.command(name="cat",description="shows up your commands")
    async def app_cat(self,interaction: discord.Interaction, table:str, request:str):

            ''' executing an SQLite command that shows up the command next to it its content in one column.
                And then wrap it in a tuple'''
            val: List = showup(table,request)
            await interaction.response.send_message(f'{val[1]}: {val[0]}')

    @app_cat.autocomplete('table')
    async def table_autocomplete(self,interaction: discord.Interaction, current: str):
        choices = tables()
        if current == "":
            choices = [app_commands.Choice(name=choice[0], value=choice[0]) for choice in choices][:25]
            return choices
        choices = [app_commands.Choice(name=choice[0], value=choice[0]) for choice in choices if 60 < match(choice[0],current) <= 100][:25]
        return choices

    @app_cat.autocomplete('request')
    async def req_autocomplete(self,interaction: discord.Interaction, current: str):
        table = interaction.data['options'][0]['value']
        choices = fetch(table)
        if current == "":
            choices = [app_commands.Choice(name=choice[0], value=choice[0]) for choice in choices][:25]
            return choices

        choices = [app_commands.Choice(name=choice[0], value=choice[0]) for choice in choices if 60 < match(choice[0],current) <= 100][:25]

        return choices

async def setup(bot):
    await bot.add_cog(cat(bot))

import discord
from discord import app_commands
from discord.ext import commands
from extras.utils.sql import *



class Add_cmd(discord.ui.Modal, title="Adding other commands or groups"):
    CmdGroup = discord.ui.TextInput(label="Command's group",placeholder="group name here.")
    Cmdname = discord.ui.TextInput(label="Command to add",placeholder="command name here.")
    CmdContent = discord.ui.TextInput(label="Command's Content",placeholder="content to add.",style=discord.TextStyle.paragraph)
    async def on_submit(self, interaction: discord.Interaction):
        try:

            add(self.CmdGroup,self.Cmdname,self.CmdContent)
            await interaction.response.send_message('Command added.', ephemeral=True)

        except sqlite3.OperationalError:
            await interaction.response.send_message('Failed to delete command. It can be either due to an invalid command name or invalid group name.')


class Del_cmd(discord.ui.Modal, title="Deleting internal commands or groups"):
    CmdGroup = discord.ui.TextInput(label="Command's group",placeholder="group name here.")
    Cmdname = discord.ui.TextInput(label="Command to delete",placeholder="command name here.")
    async def on_submit(self, interaction: discord.Interaction):
        try:
            delete(self.CmdGroup,self.Cmdname)
            await interaction.response.send_message('Command Deleted.', ephemeral=True)

        except sqlite3.OperationalError:
            await interaction.response.send_message('Failed to delete command. It can be either due to an invalid command name or invalid group name.',ephemeral=True)


def create_modal(group, name):
    class Mod2_cmd(discord.ui.Modal, title="Modifying..."):
        CmdContent = discord.ui.TextInput(
            label="Command's Content",
            default=showup(group, name)[0],
            style=discord.TextStyle.paragraph
        )

        def __init__(self):
            super().__init__()
            self.group = group
            self.name = name
        async def on_submit(self, interaction: discord.Interaction):
            update(self.group,self.name,self.CmdContent)
            await interaction.response.send_message("Message has been modified successfully.")

    return Mod2_cmd()


class Mod_cmd(discord.ui.Modal, title="Modifying internal commands or groups"):
    CmdGroup = discord.ui.TextInput(label="command's group",placeholder="group name here.")
    Cmdname = discord.ui.TextInput(label="command to modify",placeholder="command name here.")
    async def on_submit(self, interaction: discord.Interaction):
        button = ModButton(self.CmdGroup,self.Cmdname)
        await interaction.response.send_message("please click on this button in order to continue modifying.",view=button)


class CmdButtons(discord.ui.View):
    @discord.ui.button(label="Add",style=discord.ButtonStyle.success)
    async def add(self,interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.send_modal(Add_cmd())

    @discord.ui.button(label="Modify",style=discord.ButtonStyle.blurple)
    async def mod(self,interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.send_modal(Mod_cmd())

    @discord.ui.button(label="Delete",style=discord.ButtonStyle.danger)
    async def Del(self,interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.send_modal(Del_cmd()) # Lesson learnt: always call the instance of the class, not the class itself. dummy :p

class ModButton(discord.ui.View):
    def __init__(self,group,name):
        super().__init__()
        self.group = group
        self.name = name
    @discord.ui.button(label="Continue modifying",style=discord.ButtonStyle.grey)
    async def mod2(self,interaction: discord.Interaction,button: discord.ui.Button):
        await interaction.response.send_modal(create_modal(self.group,self.name))

class Change(commands.Cog):
    @commands.command()
    async def change(self,ctx):
        buttons = CmdButtons()
        await ctx.send('please choose one of the below.',view=buttons)

    @app_commands.command(name="add",description="adds some commands.")
    async def add(self,interaction):
        await interaction.response.send_modal(Add_cmd())

    @app_commands.command(name="rm",description="removes some commands.")
    async def rm(self,interaction):
        await interaction.response.send_modal(Del_cmd())

    @app_commands.command(name="mod",description="modifies some commands.")
    async def mod(self,interaction):
        await interaction.response.send_modal(Mod_cmd())

from nextcord import Interaction
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import guild_ids
import csv


class getRole(commands.Cog, name = "csv"):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(name="pear", description="ping pong", guild_ids=guild_ids)
    async def slashping(self, ctx: Interaction):
        
        roles = ctx.guild.roles
        fileName = "roles.csv"

        with open(fileName) as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(roles)

       
        await ctx.response.send_message(csvfile)


   
        

def setup(bot: commands.Bot):
    bot.add_cog(getRole(bot))
from nextcord import Interaction
import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import Bot
from config import guild_ids


class getRoles(commands.Cog, name = "Slash Ping"):
    def __init__(self, bot: Bot):
        self.bot = bot

    @nextcord.slash_command(name="apples", description="ping pong", guild_ids=guild_ids)
    async def slashping(self, ctx: Interaction, arg):
        roleId = 1022592943137226820
        role = ctx.guild.roles
        print(role)
        await ctx.response.send_message(role[5])
            
        

def setup(bot: commands.Bot):
    bot.add_cog(getRoles(bot))
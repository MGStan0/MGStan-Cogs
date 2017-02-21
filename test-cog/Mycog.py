import discord
from discord.ext import commands

class playnow:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def playnow(self, ctx):
        """Stops playback then starts new track!"""
        audio = self.bot.get_cog(Audio)

        #Your code will go here

        audio.Audio.stop()
        await self.bot.say("Stopping now and...")

        audio.Audio.local(ctx)
        await self.bot.say("playing local playlist!")

def setup(bot):
    bot.add_cog(Mycog(bot))

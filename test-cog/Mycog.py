import discord
from discord.ext import commands

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot


    @commands.command(pass_context=True)
    async def playnow(self, ctx):
        """Stops playback then starts new local playlist!"""

        #get functions from the audio cog
        try:
            audio = self.bot.get_cog('Audio')
        except:
            await self.bot.say('The Audio cog is not loaded')

        #stop current music and clear queue
        await.self.bot.say('Attempting to run...')
        audio.stop()
        await self.bot.say('Stopping now and...')

        audio.local(ctx)
        await self.bot.say('playing local playlist!')

def setup(bot):
    bot.add_cog(Mycog(bot))

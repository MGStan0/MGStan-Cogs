import discord
from discord.ext import commands
import threading
import os
from random import shuffle, choice
from cogs.utils.dataIO import dataIO
from cogs.utils import checks
from cogs.utils.chat_formatting import pagify
from urllib.parse import urlparse
from __main__ import send_cmd_help, settings
from json import JSONDecodeError
import re
import logging
import collections
import copy
import asyncio
import math
import time
import inspect
import subprocess
from .audio import *

class Mycog:
    """My custom cog that does stuff!"""

    def __init__(self, bot):
        self.bot = bot


    @commands.group(pass_context=True)
    async def playnow(self, ctx):
        """Stops playback then starts new local playlist!"""
        await self.bot.say('Attempting to run...')



"""
        #get functions from the audio cog
        try:
            audio = self.bot.get_cog('Audio')
        except:
            await self.bot.say('The Audio cog is not loaded')

        #stop current music and clear queue

        audio.stop()
        await self.bot.say('Stopping now and...')

        audio.local(ctx)
        await self.bot.say('playing local playlist!')
        """

def setup(bot):
    bot.add_cog(Mycog(bot))

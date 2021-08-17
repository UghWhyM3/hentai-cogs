import asyncio
import aiohttp
import discord

from redbot.core import commands

import random


class Hentai(commands.Cog):
    """(.)(.)"""

    def __init__(self, bot):
        self.bot = bot
        self._session = aiohttp.ClientSession()

    async def cog_check(self, ctx):
        return ctx.guild is None or ctx.channel.is_nsfw()

    @commands.command()
    async def hentai(self, ctx):
        """Get hentai"""
        images = [
            "https://cdn.discordapp.com/attachments/872703562168291362/877037988553572412/sample_ff73b52e844f77b41f27529bbddbbd24.png",
            "https://cdn.discordapp.com/attachments/872703562168291362/876978349975695390/8jcrubk2yph71.png"
        ]
        await self.maybe_send_embed(ctx, "Hentai!", random.choice(images))

    async def maybe_send_embed(self, ctx: commands.Context, title: str, url: str):
        kwargs = {"content": f"**{title}**\n\n{url}"}
        if await ctx.embed_requested():
            embed = discord.Embed(
                title=title,
                colour=await ctx.embed_colour()
            ).set_image(url=url)
            kwargs = {"embed": embed}
        await ctx.send(**kwargs)

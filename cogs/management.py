import asyncio

import discord
import git
from discord.ext import commands
from discord.ext.commands.errors import BadArgument

from .utils.checks import is_bot_owner_check


class Management(commands.Cog):
    """
    Set of commands for Administration.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, exception):
        message_sent = False
        if isinstance(exception, BadArgument):
            embed = discord.Embed(title=f"Error: {exception}", color=discord.Color.red())
            message = await ctx.send(embed=embed)
            message_sent = True

        if isinstance(exception, discord.Forbidden):
            embed = discord.Embed(title="Command Error!",
                                  description="I do not have permissions to do that",
                                  color=discord.Color.red())
            message = await ctx.send(embed=embed)
            message_sent = True

        if isinstance(exception, discord.HTTPException):
            embed = discord.Embed(title="Command Error!",
                                  description="Failed to preform that action, there was a Discord API error. "
                                              "Try again in a second",
                                  color=discord.Color.red())
            message = await ctx.send(embed=embed)
            message_sent = True

        if message_sent:
            await asyncio.sleep(5)
            await message.delete()

    @is_bot_owner_check()
    @commands.command(name='gitpull')
    async def git_pull(self, ctx):
        git_dir = "./"
        try:
            g = git.cmd.Git(git_dir)
            updates = g.pull()
            embed = discord.Embed(title="Successfully pulled from repository", color=discord.Color.green(),
                                  description=f"```{updates}```")
            await ctx.channel.send(embed=embed)

        except Exception as e:
            errno, strerror = e.args
            embed = discord.Embed(title="Command Error!",
                                  description=f"Git Pull Error: {errno} - {strerror}",
                                  color=discord.Color.red())
            await ctx.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Management(bot))

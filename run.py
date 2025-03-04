import os
from pathlib import Path
import sys
import traceback
import aiohttp

from discord import (Game, HTTPException, Intents, Interaction, Message,
                     Status, app_commands, ActivityType, activity, CustomActivity, Activity, BaseActivity, )
from discord.ext import commands
from dotenv import load_dotenv

from debug import DebugView
from utility.utils import errEmbed

load_dotenv()
token = os.getenv('TOKEN')

# 前綴, token, intents
intents = Intents.default()
intents.members = True
intents.reactions = True
intents.message_content = True
intents.presences = True

class KanadeBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=['!','%'],
            intents=intents,
            application_id=os.getenv('APP_ID')
        )
        
    async def setup_hook(self) -> None:
        self.repeat = False
        self.prev = False
        self.session = aiohttp.ClientSession()
        await self.load_extension('jishaku')
        for filepath in Path('./cogs').glob('**/*.py'):
            cog_name = Path(filepath).stem
            await self.load_extension(f'cogs.{cog_name}')

    async def on_ready(self):
        await self.change_presence(
            status=Status.online,
            activity=Activity,
            type=ActivityType.listening, 
            name=f'カナデトモスソ'  
            )
        print(f'Logged in as {self.user}')

    async def on_message(self, message: Message):
        if message.author.id == self.user.id:
            return
        await self.process_commands(message)

    async def on_command_error(self, ctx, error) -> None:
        if hasattr(ctx.command, 'on_error'):
            return
        ignored = (commands.CommandNotFound, )
        error = getattr(error, 'original', error)
        if isinstance(error, ignored):
            return
        if isinstance(error, commands.DisabledCommand):
            await ctx.send(f'{ctx.command} has been disabled.')
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
            except HTTPException:
                pass
        else:
            print('Ignoring exception in command {}:'.format(
                ctx.command), file=sys.stderr)
            traceback.print_exception(
                type(error), error, error.__traceback__, file=sys.stderr)

    async def close(self) -> None:
        self.session.close()
        return await super().close()


bot = KanadeBot()
tree = bot.tree


@tree.error
async def err_handle(i: Interaction, e: app_commands.AppCommandError):
    if isinstance(e, app_commands.errors.MissingRole):
        embed = errEmbed(message='你不是小雪團隊的一員').set_author(
            name='權限不足', icon_url=i.user.avatar)
        if i.response._responded:
            await i.edit_original_message(embed=embed)
        else:
            await i.response.send_message(embed=embed, ephemeral=True)
    else:
        ayaakaa = i.client.get_user(831883841417248778)
        view = DebugView(traceback.format_exc())
        embed = errEmbed(message=f'```py\n{e}\n```').set_author(
            name='未知錯誤', icon_url=i.user.avatar)
        await i.channel.send(content=f'{ayaakaa.mention} 系統已將錯誤回報給綾霞, 請耐心等待修復', embed=embed, view=view)

bot.run(token)

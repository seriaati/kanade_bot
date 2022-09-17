import discord
from discord import app_commands, embeds, Embed
from discord.ext import commands
from discord.app_commands import Choice

import aiohttp

from utility.apps.sekai.user.data_processing import (get_user_game_data, get_user_profile, get_user_decks, get_user_profile_pic)
from utility.utils import defaultEmbed

async def user_profile(import_id: int, session: aiohttp.ClientSession):
    user_id = 244775114281091084 
    if user_id == await get_user_game_data(import_id, 'userId', session):
        name = await get_user_game_data(import_id, 'name', session)
        id = user_id
        rank = await get_user_game_data(import_id, 'rank', session)
        word = await get_user_profile(import_id, 'word', session)
        twitter_id = await get_user_profile(import_id, 'twitterId', session) 
        leader_id = await get_user_decks(import_id, 'leader', session)
        img_url = await get_user_profile_pic(import_id, leader_id, session)       
        
        if word == None or len(word) < 1: word = 'none'
        
        embed = defaultEmbed(title=f'**{name}**', description=f'「{word}」')
        embed.set_thumbnail(url=img_url)
        embed.add_field(name=f'等級：', value=f'{rank}', inline=False)
        if twitter_id != None or len(twitter_id) >= 1: 
            embed.add_field(name=f'Twitter：', value=f'{twitter_id}', inline=False)
        embed.add_field(name=f'Id：', value=f'`{id}`', inline=False)

        return embed
    
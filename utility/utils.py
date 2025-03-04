from datetime import datetime

import discord

from data.version import version

def defaultEmbed(title: str = '', description: str = '', url: str = ''):
    embed = discord.Embed(title=title, description=description, url=url, color=0xBB6688)
    return embed

def updateEmbed(description: str = ''):
    embed = discord.Embed(title=f'**奏寶 v{version}**', description=description, color=0xBB6688)
    embed.set_author(name="奏寶", url="https://github.com/Ayaakaa/kanade_bot",
                         icon_url="https://i.imgur.com/oXEl8tP.jpg")
    embed.set_image(url="https://i.imgur.com/1SJ6Y0Y.jpg")
    embed.set_footer(text=f"奏寶 - by Ayaakaa@Seria Studios",
                     icon_url="https://imgur.com/HwcMqPS.png")
    return embed

def errEmbed(title: str = '', message: str = ''):
    return discord.Embed(title=title, description=message, color=0xfc5165)


def log(is_system: bool, is_error: bool, log_type: str, log_msg: str):
    now = datetime.now()
    today = datetime.today()
    current_date = today.strftime('%Y-%m-%d')
    current_time = now.strftime("%H:%M:%S")
    system = "SYSTEM"
    if not is_system:
        system = "USER"
    if not is_error:
        log_str = f"<{current_date} {current_time}> [{system}] ({log_type}) {log_msg}"
    else:
        log_str = f"<{current_date} {current_time}> [{system}] [ERROR] ({log_type}) {log_msg}"
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{log_str}\n')
    return log_str


def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

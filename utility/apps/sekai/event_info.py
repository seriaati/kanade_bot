import re, aiohttp
from utility.apps.sekai.api_functions import get_sekai_events_api_jp, get_sekai_event_deck_bonuses_api_jp, \
    get_sekai_events_api_tw, get_sekai_event_deck_bonuses_api_tw, get_sekai_characters_info_api

#jp
async def get_event_info_jp(session: aiohttp.ClientSession):
    event_api = await get_sekai_events_api_jp(session)
    event_id = event_api[-1]['id']
    event_name = event_api[-1]['name']
    event_type = event_api[-1]['eventType'].capitalize()
    event_start_time = event_api[-1]['startAt']
    event_end_time = event_api[-1]['aggregateAt']
    event_banner_name = event_api[-1]['assetbundleName']
    
    event_api = await get_sekai_event_deck_bonuses_api_jp(session)
    event_bonus_attribute = event_api[-1]['cardAttr'].capitalize()
    
    event_api = await get_sekai_event_deck_bonuses_api_jp(session)
    characters_id_list = []
    for thing in event_api:
        if event_id == thing['eventId']:
            character_id = thing.get('gameCharacterUnitId')
            characters_id_list.append(character_id)
    if None in characters_id_list:
        characters_id_list.remove(None)
    characters_id_list = list(dict.fromkeys(characters_id_list))
    
    characters_name_list = []
    event_api = await get_sekai_characters_info_api(session)
    for character_id in characters_id_list:
        for thing in event_api:
            if character_id == thing['id']:
                first_name = thing['firstName']
                last_name = thing['givenName']
                name = f'{first_name}{last_name}'
                characters_name_list.append(name)
    if None in characters_name_list:
        characters_name_list.remove(None)
    
    event_info = {
        'event_id': event_id,
        'event_name': event_name,
        'event_type': event_type,
        'event_start_time': event_start_time,
        'event_end_time': event_end_time,
        'event_banner_name': event_banner_name,
        'event_bonus_attribute': event_bonus_attribute,
        'characters_name_list': characters_name_list        
    }
    return event_info
#tw
async def get_event_info_tw(session: aiohttp.ClientSession):
    event_api = await get_sekai_events_api_tw(session)
    event_id = event_api[-1]['id']
    event_name = event_api[-1]['name']
    event_type = event_api[-1]['eventType'].capitalize()
    event_start_time = event_api[-1]['startAt']
    event_end_time = event_api[-1]['aggregateAt']
    event_banner_name = event_api[-1]['assetbundleName']
    
    event_api = await get_sekai_event_deck_bonuses_api_tw(session)
    event_bonus_attribute = event_api[-1]['cardAttr'].capitalize()
    
    event_api = await get_sekai_event_deck_bonuses_api_tw(session)
    characters_id_list = []
    for thing in event_api:
        if event_id == thing['eventId']:
            character_id = thing.get('gameCharacterUnitId')
            characters_id_list.append(character_id)
    if None in characters_id_list:
        characters_id_list.remove(None)
    characters_id_list = list(dict.fromkeys(characters_id_list))
    
    characters_name_list = []
    event_api = await get_sekai_characters_info_api(session)
    for character_id in characters_id_list:
        for thing in event_api:
            if character_id == thing['id']:
                first_name = thing['firstName']
                last_name = thing['givenName']
                name = f'{first_name}{last_name}'
                characters_name_list.append(name)
    if None in characters_name_list:
        characters_name_list.remove(None)
    
    event_info = {
        'event_id': event_id,
        'event_name': event_name,
        'event_type': event_type,
        'event_start_time': event_start_time,
        'event_end_time': event_end_time,
        'event_banner_name': event_banner_name,
        'event_bonus_attribute': event_bonus_attribute,
        'characters_name_list': characters_name_list        
    }
    return event_info
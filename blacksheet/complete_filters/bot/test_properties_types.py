import datetime
import telebot
import time
import json

from telebot import types
from telebot.apihelper import ApiTelegramException
from requests.exceptions import ConnectionError, ReadTimeout
from json_healer import heal

from Strings_Data import strings_data as strings




def try_str( string_data, id, default ):

    try:
        assert string_data[id] != None 
        return string_data[id]
    except:
        return default




class FiltersBot():

    def __init__( self, bot_key ) -> None:
        self.bot = telebot.TeleBot( bot_key )
        self.starter_text = "выберите желаемое действие в меню"
        self.search_menu_text = "задайте параметры поиска и нажмите \"сохранить\""


    def get_filter_blocks( self ):

        """мдея в том, чтобы оптиммзировать частоту запросов набора фильтров"""

        import requests #FIXME:is it ok???????

        headers = {
            'authority': 'api.av.by',
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
            'content-type': 'application/json',
            'dnt': '1',
            'origin': 'https://av.by',
            'referer': 'https://av.by/',
            'sec-ch-ua': '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36',
            'x-api-key': '5f76cde7ebefc9.04631320',
            'x-device-type': 'web.desktop',
        }

        response = requests.get('https://api.av.by/home/filters/home/init', headers=headers)
        r_content = json.loads( response.content )["blocks"] #FIXME: try except
        response.close()

        return r_content


    def get_properties( self ) :

        blocks = self.get_filter_blocks()
        prop_types = []
        prop_counts = {}  
        prop_names = {}      
        
        for group in blocks :            
            for row in group["rows"] :
                for propertyGroup in row["propertyGroups"] :
                    for property in propertyGroup["properties"]:


                        if not property["fallbackType"] in prop_types:
                            prop_types.append( property["fallbackType"] )


                        if not property["fallbackType"] in prop_counts.keys() :
                            prop_counts[ property["fallbackType"] ] = 0

                        prop_counts[ property["fallbackType"] ] += 1  


                        if not property["fallbackType"] in prop_names.keys() :
                            prop_names[ property["fallbackType"] ] = {}

                        prop_names[ property["fallbackType"] ][ property["name"] ] = None

            
        return ( prop_types, prop_counts, prop_names )


bot = FiltersBot( bot_key= "null" )
prop_data = bot.get_properties()
print( json.dumps( prop_data[2], indent=4 ) )        
import datetime
import telebot
import time
import json

from telebot import types
from telebot.apihelper import ApiTelegramException
from requests.exceptions import ConnectionError, ReadTimeout
from json_healer import heal

from Strings_Data import strings_data as strings


ru_strs = {}


def write_log( txt ):
    print( txt )



def try_str( string_data, id, default ):

    try:
        assert string_data[id] != None 
        return string_data[id]
    except:
        return default




class SASS_bot():

    def __init__( self, bot_key ) -> None:
        self.bot = telebot.TeleBot( bot_key )
        self.bot_data = {
            "recent_id":0
        }
        self.ru_strings = {}


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
            group_question = f"ru\n{group['id']}:{group['name']}"
            self.once_aks_group_label( id = group['id'], question= group_question )          
            
            for row in group["rows"] :
                row_question = group_question + f"\n{' '*2}{row['id']}:{row['type']}:{row['label']}"
                self.once_aks_group_label( id = row['id'], question= row_question )

                for propertyGroup in row["propertyGroups"] :
                    pG_question = row_question + f"\n{' '*4}{propertyGroup['id']}:{propertyGroup['label']}"
                    self.once_aks_group_label( id= propertyGroup['id'], question= pG_question )

                    for property in propertyGroup["properties"]:
                        prop_question = pG_question + f"\n{' '*6}{ property['id'] }:{ property['name'] }"
                        self.once_aks_group_label( id= property['id'], question= prop_question )


                        """
                        if not property["fallbackType"] in prop_types:
                            prop_types.append( property["fallbackType"] )


                        if not property["fallbackType"] in prop_counts.keys() :
                            prop_counts[ property["fallbackType"] ] = 0

                        prop_counts[ property["fallbackType"] ] += 1  


                        if not property["fallbackType"] in prop_names.keys() :
                            prop_names[ property["fallbackType"] ] = {}
                        """    

                        #prop_names[ property["fallbackType"] ][ property["name"] ] = None

            
        return ( prop_types, prop_counts, prop_names )
    


    def ask( self, question, id="000", user_id=931481755 ):

        bot.bot.send_message( chat_id= user_id, text=question  )

        updates = []
        while updates == [] :
            
            #updates = bot.bot.get_updates( offset = self.bot_data["recent_id"]+1 , timeout= None, allowed_updates=["message"] )
            try:
                updates = bot.bot.get_updates( offset=self.bot_data["recent_id"]+1 , timeout= None, allowed_updates=["message"] )
            except ConnectionError :
                write_log(f"No responce [{time.asctime()}]")
            except ReadTimeout :
                write_log(f"ReadTimeout [{time.asctime()}]")   
            except ApiTelegramException as ate:
                if str(ate.error_code) != '409':
                    write_log(f"ApiTelegramException [{time.asctime()}]")


        upd = updates[0]
        answer = upd.message.text

        self.bot_data[ "recent_id" ] = upd.update_id 
        #print( upd.update_id )

        with open( R"C:\Users\nikita\Desktop\save\avby_assistant_server\v2\blacksheet\complete_filters\bot\sass_backup.txt", 'a', encoding="utf-8" ) as f :
            f.write( '"'+id+'":"' + answer + '",\n' )
            print( '"'+id+'":"' + answer + '",' )

        return answer
        
    def once_aks_group_label( self, id, question ):
        if not str(id) in self.ru_strings.keys():
            self.ru_strings[ str(id) ] = self.ask( question= question, id=str(id) )




bot = SASS_bot( bot_key= "6502695853:AAGIg5f867h7lW1HwYoT521XswWZUL0ouZM" )
prop_data = bot.get_properties()
print( json.dumps( prop_data[2], indent=4 ) ) 

print( bot.ru_strings )
import datetime
import telebot
import time
import json

from telebot import types
from telebot.apihelper import ApiTelegramException
from requests.exceptions import ConnectionError, ReadTimeout
from json_healer import heal

from userClass import User
from Strings_Data import strings_data as strings



class FiltersBot():

    def __init__( self, bot_key ) -> None:
        self.bot = telebot.TeleBot( bot_key )
        self.starter_text = "выберите желаемое действие в меню"
        self.search_menu_text = "задайте параметры поиска и нажмите \"сохранить\""

    
    def inline_builder( self, buttons_list = [[]] ):#[["<-","->"]]

        """[[ ('a0',"a0_clicked"), ('b0',"b0_clicked") ],\n
        [ ('a1',"a1_clicked"), ('b1',"b1_clicked") ]]\n\n
        button_list - list of rows\n
        row - list of buttons\n
        button - tuple of text and callback_data"""

        inline_keyboard = []
        for line in buttons_list:
            line_buttons = []
            for button_initiator in line:
                line_buttons.append( types.InlineKeyboardButton( text=button_initiator[0], callback_data=button_initiator[1] )  ) 
            inline_keyboard.append(line_buttons)    
                
        return types.InlineKeyboardMarkup(inline_keyboard)
    


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
    
        """import requests

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

        json_data = {
            'properties': [
                {
                    'modified': True,
                    'name': 'brands',
                    'property': 6,
                    'value': [
                        [
                            {
                                'name': 'brand',
                                'value': 6,
                                'modified': True,
                                'previousValue': None,
                            },
                        ],
                    ],
                },
                {
                    'name': 'price_currency',
                    'value': 2,
                },
            ],
        }

        response = requests.post('https://api.av.by/home/filters/home/update', headers=headers, json=json_data)

        # Note: json_data will not be serialized by requests
        # exactly as it was in the original request.
        #data = '{"properties":[{"modified":true,"name":"brands","property":6,"value":[[{"name":"brand","value":6,"modified":true,"previousValue":null}]]},{"name":"price_currency","value":2}]}'
        #response = requests.post('https://api.av.by/home/filters/home/update', headers=headers, data=data)
        """

    def back_button( self, upd_data ):
        ds = ""
        for r in upd_data.split('.')[:-1:] :
            ds += r + '.'
          
        return types.InlineKeyboardButton( text="назад", callback_data= ds[:-1:] )  
    

    def starter( self, user_id ):

        starter_markup = self.inline_builder( [
            [( "новый поиск", "new_search" )]
        ] )

        self.bot.send_message( chat_id=user_id, text= self.starter_text, reply_markup= starter_markup )
        print( starter_markup.keyboard[0][0] )# FIXME delete



    def search_menu( self, upd ):

        search_menu_markup = self.inline_builder( [
            [( "модель", "BMG_menu" )],
            [( "год\\цена\\объём", "summary_menu" )],
            [( "расширенные", "extended_menu" )],
            [( "сохранить", "save" )]
        ] )

        self.bot.edit_message_text( text= self.search_menu_text, chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= search_menu_markup )


    def search_menu_2( self, upd ):

        blocks = self.get_filter_blocks()
        inline = types.InlineKeyboardMarkup()

        for i in blocks :
            if type(i) is dict :
                inline.add( types.InlineKeyboardButton( text= try_str( strings.en, id=str(i["id"]), default= i["name"] ) , callback_data=  upd.callback_query.data+'.'+str(i['id']) ) )#+i['name']
                #try:
                #    assert strings.en[ str(i["id"]) ] != None
                #    inline.add( types.InlineKeyboardButton( text = strings.en[ str(i["id"]) ], callback_data= f"""{ upd.callback_query.data }.{ i['name'] }""" ) )   
                #except:     
                #    inline.add( types.InlineKeyboardButton( text=i["name"], callback_data= upd.callback_query.data+'.'+i['name'] ) )

        #inline.add( self.back_button( upd_data=upd.callback_query.data ) ) 
        # save ?
        # cancel ?     

        self.bot.edit_message_text( text= self.search_menu_text, chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )



    def rows_in_group( self, upd ) :
        
        blocks = self.get_filter_blocks()
        group = None
        for g in blocks :
            
            if str(g["id"]) == upd.callback_query.data.split('.')[1] : #FIXME: optimize?
                group = g
                break #FIXME: maybe "blocks = []"?

        if group != None :
            inline = types.InlineKeyboardMarkup()

            for row in group["rows"] :
                inline.add( types.InlineKeyboardButton( text=  try_str( strings.en, str(row["id"]), default= f"""{row["id"]}:{row["type"]}:{row["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ row['id'] }""" ) )
                    
            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= try_str(  strings.en, str(group["id"]), default=  f"""{ group["id"] }:{ group["name"] }""" ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           
            

    def propertyGroups_in_row( self, upd ) :

        blocks = self.get_filter_blocks()
        
        group = None
        for g in blocks :            
            if str(g["id"]) == upd.callback_query.data.split('.')[1] : #FIXME: optimize?
                group = g
                break #FIXME: maybe "blocks = []"?
        
        row = None    
        for r in group["rows"] :
            if str(r['id']) == upd.callback_query.data.split('.')[2]:
                row = r
                break #FIXME: maybe "blocks = []"?

        if row != None:
            inline = types.InlineKeyboardMarkup()

            for propertyGroup in row["propertyGroups"]:
                inline.add( types.InlineKeyboardButton( text=  try_str( strings.en, str(propertyGroup["id"]), default= f"""{propertyGroup["id"]}:{propertyGroup["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ propertyGroup['id'] }""" ) )

            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= try_str(  strings.en, str(row["id"]), default=  f"""{ row["id"] }:{ row["type"] }:{ row["label"] }""" ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



    def properties_in_pG( self, upd ) :

        blocks = self.get_filter_blocks()
        
        group = None
        for g in blocks :            
            if str(g["id"]) == upd.callback_query.data.split('.')[1] : #FIXME: optimize?
                group = g
                break #FIXME: maybe "blocks = []"?
        
        row = None    
        for r in group["rows"] :
            if str(r['id']) == upd.callback_query.data.split('.')[2]:
                row = r
                break #FIXME: maybe "blocks = []"?

        propertyGroup = None    
        for pg in row["propertyGroups"] :
            if str(pg['id']) == upd.callback_query.data.split('.')[3]:
                propertyGroup = pg
                break #FIXME: maybe "blocks = []"?  

        if propertyGroup != None :
            inline = types.InlineKeyboardMarkup()

            for property in propertyGroup["properties"]:

                match property['fallbackType']:
                    
                    case 'boolean' :

                        status_symb = strings.sys["disabled_symb"]                        
                        if users[str( upd.callback_query.message.chat.id )].new_search["boolean"][  property['name']  ] == True :
                            status_symb = strings.sys["enabled_symb"]
                            
                        inline.add( types.InlineKeyboardButton( text= status_symb + try_str( strings.en, property["id"], default=f"{property['id']}:{property['name']}:{property['fallbackType']}" ), callback_data= f"""{ upd.callback_query.data }.{ property['id'] }""" ) )

                    case _:
                        inline.add( types.InlineKeyboardButton( text= try_str( strings.en, property["id"], default=f"{property['id']}:{property['name']}:{property['fallbackType']}" ), callback_data= f"""{ upd.callback_query.data }.{ property['id'] }""" ) )

            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= try_str(  strings.en, str(propertyGroup["id"]), default=  f"""{ propertyGroup["id"] }:{ propertyGroup["label"] }""" ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           


    def property_action( self, upd ) :

        blocks = self.get_filter_blocks()
        
        group = None
        for g in blocks :            
            if str(g["id"]) == upd.callback_query.data.split('.')[1] : #FIXME: optimize?
                group = g
                break #FIXME: maybe "blocks = []"?
        
        row = None    
        for r in group["rows"] :
            if str(r['id']) == upd.callback_query.data.split('.')[2]:
                row = r
                break #FIXME: maybe "blocks = []"?

        propertyGroup = None    
        for pg in row["propertyGroups"] :
            if str(pg['id']) == upd.callback_query.data.split('.')[3]:
                propertyGroup = pg
                break #FIXME: maybe "blocks = []"?  

        #prop = None    
        for p in propertyGroup["properties"] :
            if str(p['id']) == upd.callback_query.data.split('.')[4]:
                #prop = p
                #switch
                if users[str( upd.callback_query.message.chat.id )].new_search['boolean'][  p['name']  ] == None :
                    users[str( upd.callback_query.message.chat.id )].new_search['boolean'][  p['name']  ] = True
                else:
                    users[str( upd.callback_query.message.chat.id )].new_search['boolean'][  p['name']  ] = None    
                break #FIXME: maybe "blocks = []"?    

        if propertyGroup != None :
            inline = types.InlineKeyboardMarkup()

            for property in propertyGroup["properties"]:

                match property['fallbackType']:
                    
                    case 'boolean' :

                        status_symb = strings.sys["disabled_symb"]                        
                        if users[str( upd.callback_query.message.chat.id )].new_search['boolean'][  property['name']  ] == True :
                            status_symb = strings.sys["enabled_symb"]

                        #self.back_button(upd.callback_query.data).callback_data    
                        inline.add( types.InlineKeyboardButton( text= status_symb + try_str( strings.en, property["id"], default=f"{property['id']}:{property['name']}:{property['fallbackType']}" ), callback_data= f"""{ self.back_button(upd.callback_query.data).callback_data }.{ property['id'] }""" ) )

                    case _:
                        inline.add( types.InlineKeyboardButton( text= try_str( strings.en, property["id"], default=f"{property['id']}:{property['name']}:{property['fallbackType']}" ), callback_data= f"""{ upd.callback_query.data }.{ property['id'] }""" ) )

            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= try_str(  strings.en, str(propertyGroup["id"]), default=  f"""{ propertyGroup["id"] }:{ propertyGroup["label"] }""" ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           






    def filter_menu( self, upd ):

        blocks = self.get_filter_blocks()

        for key in upd.callback_query.data.split('.')[1::] :

            for i in blocks :
                if type(i) is dict and i["name"]==key:

                    blocks = i["rows"]

        inline = types.InlineKeyboardMarkup()
        for i in blocks :
            if type(i) is dict :
                inline.add( types.InlineKeyboardButton( text=i["name"], callback_data= upd.callback_query.data+'.'+i['name'] ) )

        inline.add( self.back_button( upd_data=upd.callback_query.data ) )

        self.bot.edit_message_text( text= self.search_menu_text, chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )
            




def try_str( string_data, id, default ):

    try:
        assert string_data[id] != None 
        return string_data[id]
    except:
        return default
        



def write_log(text):
    print(text)





def get_upd_type( upd, default=False):
                            
    if upd.message != None:
        upd_type = f"'{ str(upd.message.content_type) }'"

        if upd.message.content_type == "text" and upd.message.text[0] == '/' :
            upd_type = "command"

        return upd_type    

    elif upd.edited_message != None:
        upd_type = "edited_message"
        return upd_type

    elif upd.callback_query != None:
        upd_type = "callback_query" # na koj lyad??
        return upd_type

    return default







#bot = FiltersBot( bot_key= "6378927209:AAFN58sc6C5qyfsBJP1GJOp5ab8GWtheI6w")
token = "6502695853:AAGIg5f867h7lW1HwYoT521XswWZUL0ouZM"
bot = FiltersBot( bot_key= token )

class debil():
    def __init__(self, id) -> None:
        self.id = id

users = {
    "931481755":User( debil(931481755) )
}

json_data = {
    "recent_id": 0
}

print("started")


while True:

    updates = []

    try:
        updates = bot.bot.get_updates( offset=json_data["recent_id"]+1 , timeout= None, allowed_updates= [ "message", "callback_query" ] )
        if updates != [] :
            print( "new" )
    except ConnectionError :
        write_log(f"No responce [{time.asctime()}]")
    except ReadTimeout :
        write_log(f"ReadTimeout [{time.asctime()}]")   
    except ApiTelegramException as ate:
        if str(ate.error_code) != '409':
            write_log(f"ApiTelegramException [{time.asctime()}]")  
        else:       
            write_log(f"ApiTelegramException 409") 
        #print( type(ate) ) 
        #print( ate.error_code )



    for upd in updates :
        print('got upd')

        upd_source = None

        try:
            upd_type = get_upd_type( upd, default="not define" )
        except:
            write_log( f"   Warning: can't define upd type. UPD:{str(upd)}" )


        with open( "C:\\Users\\nikita\\Desktop\\save\\avby_assistant_server\\v2\\blacksheet\\complete_filters\\bot\\upd.json", "w", encoding="utf-8" ) as f:
            f.write( heal( str(upd) ) )

        
        
        match upd_type:

            
            
            
            
            case "command":
                upd_source = str(upd.message.chat.id)
                match upd.message.text :

                    case "/start":

                        try:
                            nothing = users[ str( upd.message.chat.id ) ]
                        except KeyError :
                            users[ str( upd.message.chat.id ) ] = User( tg_usr= upd.message.chat )

                        bot.starter( user_id= upd.message.chat.id )

                    case "/status":
                        bot.bot.send_message( upd.message.chat.id, "камплит фильтэрс тоже воркают" )    


            
            
            
            
            
            case "callback_query":
                upd_source = str(upd.callback_query.message.chat.id)
                try:
                    bot.bot.answer_callback_query( callback_query_id= upd.callback_query.id, text= upd.callback_query.data,
                                                show_alert= False
                                            )
                except :
                    write_log( f"trouble with callback" )    
                match upd.callback_query.data.split('.')[0] :

                    case "new_search":
                        
                        match len( upd.callback_query.data.split('.') ) :
                            case 1 :
                                bot.search_menu_2( upd )
                                #bot.filter_menu( upd )

                            case 2 :
                                bot.rows_in_group( upd )

                            case 3 :
                                bot.propertyGroups_in_row( upd )

                            case 4 :
                                bot.properties_in_pG( upd )  

                            case 5 :
                                bot.property_action( upd )          



                    case _:
                        write_log( f"unknown callback: {upd.callback_query.data}" )
                        bot.bot.send_message( chat_id=upd.callback_query.message.chat.id, text=upd.callback_query.data )

            
            
            
            
            
            
            case _:
                pass

        
        try:
            if upd_source != None :
                with open( R"C:\Users\nikita\Desktop\save\users.json", "r", encoding="utf-8" ) as f:
                    jd = json.load( f )
                    f.close()

                if not upd_source in jd.keys():
                    jd[upd_source] = [ ]

                if not token in jd[upd_source] :
                    # jd[upd_source] = jd[upd_source].copy().append( token ) -> None
                    jd[upd_source].append( token )

                    with open( R"C:\Users\nikita\Desktop\save\users.json", "w", encoding="utf-8" ) as f:
                        json.dump( jd, f )
                        f.close()

        except:
            write_log( f"failed writing source({upd_source}) to sources" )



        json_data["recent_id"] = upd.update_id        
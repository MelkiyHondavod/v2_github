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


class debil():
    def __init__(self, id) -> None:
        self.id = id


class FiltersBot():

    def __init__( self, bot_key ) -> None:
        self.bot = telebot.TeleBot( bot_key )
        self.starter_text = "выберите желаемое действие в меню"
        self.search_menu_text = "задайте параметры поиска и нажмите \"сохранить\""
        self.users = {
            "931481755":User( debil(931481755), lang="ru" )
        }

    
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

    def back_button( self, upd_data, indexes_to_remove=1 ):
        ds = ""
        for r in upd_data.split('.')[:-indexes_to_remove:] :
            ds += r + '.'
          
        if ds == "" :
            ds = upd_data

        ds = ds[:-1:]    

        return types.InlineKeyboardButton( text="назад", callback_data= ds ) #callback_data= ds[:-1:] ? 
    

    def starter( self, user_id ):

        starter_markup = self.inline_builder( [
            [( "новый поиск", "start.new_search" )]
        ] )

        self.bot.send_message( chat_id=user_id, text= self.starter_text, reply_markup= starter_markup )
        print( starter_markup.keyboard[0][0] )# FIXME delete


    def menu_navigation( self, upd ) :

        blocks = self.get_filter_blocks()
        

        c=2 # 0 = start, 1 = new_search
        c_lim = 5
        groups = blocks
        while c<len(upd.callback_query.data.split('.')) and c<c_lim : # c<4  and   # 4 because: id, rows, propertGroups, properties
            for g in groups :
                if str(g["id"]) == upd.callback_query.data.split('.')[ c ]:
                    
                    for sub_g in g.values() :
                        if type( sub_g ) == list :
                            groups = sub_g
                            c+=1
                            #print(c)
                            break # there is not problem yet but point: property contain several lists

                    break      


        try:
            usr_lang = self.users[str( upd.callback_query.from_user.id )]
            match usr_lang:
                case "ru":
                    lang_strings = strings.ru
                case "en":
                    lang_strings = strings.en
                case _ :
                    raise 
        except:
            lang_strings = strings.ru  #default #FIXME



        if len(upd.callback_query.data.split('.')) >= 6 :
            self.propety_proc( upd, properties=groups, lang_strings=lang_strings, c=c  )

        else:

            inline = types.InlineKeyboardMarkup()

            for gr_item in groups:
                inline.add( types.InlineKeyboardButton( text=  try_str( lang_strings, str(gr_item["id"]), default= f"""{gr_item["id"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ gr_item['id'] }""" ) )

            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



    def propety_proc( self, upd, properties, lang_strings, c=6 ):

        """properties = groups"""
        #FIXME: c always equal 6, isn't it ?

        for prop in properties :
                if str(prop["id"]) == upd.callback_query.data.split('.')[ c ]:

                    ### <test
                    """gd = {}
                    for k in prop.keys() :
                        if type(prop[k]) != list :
                            gd[k] = prop[k]
                        else:
                            if prop[k] == []:
                                gd[k] = []    
                            else:
                                gd[k] = ["..."]    
                    print( json.dumps( gd, ensure_ascii=False, indent=4 ) )"""
                    #self.bot.send_message( chat_id= upd.callback_query.message.chat.id, text= json.dumps( gd, ensure_ascii=False, indent=4 ) )
                    ### test/>

                    match prop["fallbackType"] :

                        case "select" :
                            
                            match prop["valueFormat"] :

                                case "range":
                                    
                                    """
                                    try:
                                        page = int(upd.callback_query.data.split('.')[6])
                                    except IndexError:
                                        page = 0

                                    self.listing( upd, lang_strings, prop, page )
                                    """

                                    print("check2")
                                    
                                    match len( upd.callback_query.data.split('.') ) : 

                                        

                                        case 6:
                                            range_keyb = self.inline_builder(
                                                [
                                                    [("от",f"{upd.callback_query.data}.min.0")],
                                                    [("до",f"{upd.callback_query.data}.max.0")]
                                                ]
                                            )

                                            range_keyb.add( self.back_button( upd_data=upd.callback_query.data ) )#FIXME: DRY?

                                            self.bot.edit_message_text( text= try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= range_keyb )           

                                        case 7:
                                            print("Error: len of callback_data in 'range' type is equal 7 it means lack of page number, what theoreticly impossible ")


                                        case 8 : #8 | 7 :
                                            try:
                                                page = int(upd.callback_query.data.split('.')[7])
                                                #print("alarm 2 Done")
                                            except IndexError:
                                                page = 0
                                                #print( "Alarm 2" )

                                            print( f"page:{page}" )    

                                            self.listing( upd, lang_strings, prop, page )

                                        case 9 :
                                            self.bot.edit_message_text( 
                                                text= f"{try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data )}\nchosen year: {upd.callback_query.data.split('.')[8]}" , 
                                                chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, 
                                                reply_markup= None)               


                                        case _:
                                            print( f"alarm:{len( upd.callback_query.data.split('.') )}" )    


                                case "array":

                                    inline = types.InlineKeyboardMarkup()

                                    for option in prop["options"]:                                                                                      #FIXME: ↓ unreliable (Am I meant key "label" is not stable ?)
                                        inline.add( types.InlineKeyboardButton( text=  try_str( lang_strings, f'{prop["id"]}.{option["id"]}', default= f"""{option["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ option['id'] }""" ) )

                                    inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
                                    self.bot.edit_message_text( text= try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



                                case "value":

                                    inline = types.InlineKeyboardMarkup()

                                    for option in prop["options"]:                                                                                      #FIXME: ↓ unreliable
                                        inline.add( types.InlineKeyboardButton( text=  try_str( lang_strings, f'{prop["id"]}.{option["id"]}', default= f"""{option["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ option['id'] }""" ) )

                                    inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
                                    self.bot.edit_message_text( text= try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           


                                case _:
                                    pass

                        case "compound_any" :
                            pass

                        case "string" :
                            pass

                        case _:
                            pass        





    def listing( self, upd, lang_strings, prop, page=0 ):

        #page




        keyb = []

        prop_options = []
        next_button = 0
        tg_inline_lim = 100
        control_buttons_number = 1 #back
        """if page>0 :
            control_buttons_number += 1 #prev_page_button 

        option_instead_prev_button=0
        if page != 0 :#FIXME why&
                option_instead_prev_button = 1 #on first page printed 98 instead of 97
                prev_button = 1
                keyb.append( [types.InlineKeyboardButton( text="prev", callback_data="prev" )] )
        """ 
        if page>0 :
                control_buttons_number += 1 #prev_page_button 
                #option_instead_prev_button = 1 #on first page printed 98 instead of 97
                prev_button = 1
                keyb.append( [types.InlineKeyboardButton( text="prev", callback_data=f"{ '.'.join( upd.callback_query.data.split('.')[:-1:] ) }.{page-1}" )] )  
        
        cb_default = 3
        cb_default = control_buttons_number
        if len( prop["options"][   0 + page*(tg_inline_lim-cb_default)   ::] ) <= tg_inline_lim-control_buttons_number :

            prop_options = prop["options"][   0 + page*(tg_inline_lim-cb_default)   ::] 

        else:
            cb_default += 1 # next page
            prop_options = prop["options"][   0 + page*(tg_inline_lim-cb_default)   :   0 + (page+1)*(tg_inline_lim-cb_default)  :]   
            next_button =  [types.InlineKeyboardButton( text="next", callback_data=f"{ '.'.join( upd.callback_query.data.split('.')[:-1:] ) }.{page+1}" )]
            print( f"280923: {0 + page*(tg_inline_lim-cb_default)} - {0 + (page+1)*(tg_inline_lim-cb_default) }" ) #97
                


        
        pair = []
        row_wide = 2
        for option in prop_options:   

            pair.append( types.InlineKeyboardButton( text=  try_str( lang_strings, f'{prop["id"]}.{option["id"]}', default= f"""{option["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ option['id'] }""" ) )

            if len( pair ) == row_wide:
                keyb.append( pair ) 
                pair = []

        if pair != []:
            keyb.append( pair )
        #<-
        #->

        if next_button != 0 :
            keyb.append( next_button )

            
        inline = types.InlineKeyboardMarkup(keyb)

        inline.add( self.back_button( upd_data=upd.callback_query.data, indexes_to_remove= len(upd.callback_query.data.split('.'))-6 ) )  #FIXME back_button in "[]" ?"
        print( "check" )
        self.bot.edit_message_text( text= try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



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






def main():
    #bot = FiltersBot( bot_key= "6378927209:AAFN58sc6C5qyfsBJP1GJOp5ab8GWtheI6w")
    token = "6502695853:AAGIg5f867h7lW1HwYoT521XswWZUL0ouZM"
    bot = FiltersBot( bot_key= token )





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
                                nothing = bot.users[ str( upd.message.chat.id ) ]
                            except KeyError :
                                bot.users[ str( upd.message.chat.id ) ] = User( tg_usr= upd.message.chat )

                            bot.starter( user_id= upd.message.chat.id )



                        case "/status":
                            bot.bot.send_message( upd.message.chat.id, "камплит фильтэрс тоже воркают" )    

                        case _:
                            print( f"unknown command: {upd.message.text}" )    


                
                
                
                
                
                case "callback_query":
                    upd_source = str(upd.callback_query.message.chat.id)
                    try:
                        bot.bot.answer_callback_query( callback_query_id= upd.callback_query.id, text= upd.callback_query.data,
                                                    show_alert= False
                                                )
                    except :
                        write_log( f"trouble with callback" ) 

                    match upd.callback_query.data.split('.')[0] :
                        
                        case "start":

                            if len(upd.callback_query.data.split('.')) > 1 :
                            
                                match upd.callback_query.data.split('.')[1] :

                                    case "new_search":

                                        bot.menu_navigation( upd )
                                        
                                        """
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
                                        """            


                                    case _:
                                        write_log( f"unknown callback: {upd.callback_query.data}" )
                                        bot.bot.send_message( chat_id=upd.callback_query.message.chat.id, text=f"unknown callback: {upd.callback_query.data}" )

                                
                            else:
                                    bot.starter( user_id= upd.callback_query.message.chat.id )   
                          


                        case _:
                            write_log( f"unknown callback: {upd.callback_query.data}" )
                            bot.bot.send_message( chat_id=upd.callback_query.message.chat.id, text=f"unknown callback: {upd.callback_query.data}" )#FIXME: dry?
                
                
                
                
                
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


if __name__=="__main__":
    main()            
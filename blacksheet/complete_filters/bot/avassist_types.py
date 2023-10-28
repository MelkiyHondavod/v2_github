import json
import telebot

from telebot import types
from Strings_Data import strings_data as strings




class User():

    def __init__( self, tg_usr, lang="en" ):
        self.id = tg_usr.id
        #self.username = tg_usr.username # can be also chat 
        self.lang = lang
        #self.subscriptions = []
        self.new_search = {
                "compound_any": {
                    "brands": None,
                    "price_compound_on_filter_form": None
                },
                "select": {
                    "year": None,
                    "engine_capacity": None,
                    "transmission_type": None,
                    "body_type": None,
                    "engine_type": None,
                    "drive_type": None,
                    "place_region": None,
                    "place_city": None,
                    "seller_type": None,
                    "condition": None,
                    "mileage_km": None,
                    "creation_date": None,
                    "registration_country": None,
                    "color": None,
                    "interior_color": None,
                    "interior_material": None
                },
                "string": {
                    "description": None
                },
                "boolean": {
                    "video_url": None,
                    "has_nds": None,
                    "has_exchange": None,
                    "vin_checked": None,
                    "registration_status_deregistered": None,
                    "alloy_wheels": None,
                    "railings": None,
                    "hitch": None,
                    "abs": None,
                    "esp": None,
                    "anti_slip_system": None,
                    "immobilizer": None,
                    "alarm": None,
                    "rain_detector": None,
                    "rear_view_camera": None,
                    "parktronics": None,
                    "mirror_dead_zone_control": None,
                    "front_safebags": None,
                    "side_safebags": None,
                    "rear_safebags": None,
                    "panoramic_roof": None,
                    "hatch": None,
                    "seven_seats": None,
                    "drive_auto_start": None,
                    "cruise_control": None,
                    "steering_wheel_media_control": None,
                    "electro_seat_adjustment": None,
                    "front_glass_lift": None,
                    "rear_glass_lift": None,
                    "seat_heating": None,
                    "front_glass_heating": None,
                    "mirror_heating": None,
                    "steering_wheel_heating": None,
                    "autonomous_heater": None,
                    "climate_control": None,
                    "conditioner": None,
                    "aux_ipod": None,
                    "bluetooth": None,
                    "cd_mp3_player": None,
                    "usb": None,
                    "media_screen": None,
                    "navigator": None,
                    "xenon_lights": None,
                    "fog_lights": None,
                    "led_lights": None
                }
            
        }
        self.SEARCH_CARD_PATTERN = {
                "compound_any": {
                    "brands": None,
                    "price_compound_on_filter_form": None
                },
                "select": {
                    "year": None,
                    "engine_capacity": None,
                    "transmission_type": None,
                    "body_type": None,
                    "engine_type": None,
                    "drive_type": None,
                    "place_region": None,
                    "place_city": None,
                    "seller_type": None,
                    "condition": None,
                    "mileage_km": None,
                    "creation_date": None,
                    "registration_country": None,
                    "color": None,
                    "interior_color": None,
                    "interior_material": None
                },
                "string": {
                    "description": None
                },
                "boolean": {
                    "video_url": None,
                    "has_nds": None,
                    "has_exchange": None,
                    "vin_checked": None,
                    "registration_status_deregistered": None,
                    "alloy_wheels": None,
                    "railings": None,
                    "hitch": None,
                    "abs": None,
                    "esp": None,
                    "anti_slip_system": None,
                    "immobilizer": None,
                    "alarm": None,
                    "rain_detector": None,
                    "rear_view_camera": None,
                    "parktronics": None,
                    "mirror_dead_zone_control": None,
                    "front_safebags": None,
                    "side_safebags": None,
                    "rear_safebags": None,
                    "panoramic_roof": None,
                    "hatch": None,
                    "seven_seats": None,
                    "drive_auto_start": None,
                    "cruise_control": None,
                    "steering_wheel_media_control": None,
                    "electro_seat_adjustment": None,
                    "front_glass_lift": None,
                    "rear_glass_lift": None,
                    "seat_heating": None,
                    "front_glass_heating": None,
                    "mirror_heating": None,
                    "steering_wheel_heating": None,
                    "autonomous_heater": None,
                    "climate_control": None,
                    "conditioner": None,
                    "aux_ipod": None,
                    "bluetooth": None,
                    "cd_mp3_player": None,
                    "usb": None,
                    "media_screen": None,
                    "navigator": None,
                    "xenon_lights": None,
                    "fog_lights": None,
                    "led_lights": None
                }
            
        }
        self.search_cards = {} # "<id>":<search_card>  id - "<chat_id>.<message_id( если удаление сообщений не ведёт к обнулению )>"

    def check_permision(self):
        return True

    def open_new_search_card(self, message_id ):

        if self.check_permision():                                            
            self.search_cards[ message_id ] = self.SEARCH_CARD_PATTERN
            return True
        
        return False


class debil():
    def __init__(self, id) -> None:
        self.id = id


class FiltersBot():

    def __init__( self, bot_key ) -> None:
        self.bot = telebot.TeleBot( bot_key )
        self.starter_text = "выберите желаемое действие в меню"
        self.search_menu_text = "задайте параметры поиска и нажмите \"сохранить\""
        self.users = {
            "931481755": User( debil(931481755), lang="ru" )
        }



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
                inline.add( types.InlineKeyboardButton( text=  Tools().try_str( lang_strings, str(gr_item["id"]), default= f"""{gr_item["id"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ gr_item['id'] }""" ) )

            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= Tools().try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



    def provide_ns_menu( self, upd ):
        
        if  self.users[str( upd.callback_query.message.chat.id )].open_new_search_card( message_id= upd.callback_query.message.id ) is True:
                                            
            self.menu_navigation( upd )       

        else:
            self.bot.answer_callback_query( callback_query_id= upd.callback_query.id, text= "Access denied :/ jr idk",
                show_alert= False
            )


    
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
    

    def back_button( self, upd_data, indexes_to_remove=1 ):
        ds = ""
        for r in upd_data.split('.')[:-indexes_to_remove:] :
            ds += r + '.'
          
        if ds == "" :
            ds = upd_data

        ds = ds[:-1:]    

        return types.InlineKeyboardButton( text="назад", callback_data= ds ) #callback_data= ds[:-1:] ? 
    

    def starter( self, upd, mode= "new" ):

        #user_id = upd.message.chat.id

        starter_markup = self.inline_builder( [
            [( "новый поиск", "start.new_search" )]
        ] )


        match mode:

            case "new": 

                user_id = upd.message.chat.id
                self.bot.send_message( chat_id=user_id, text= self.starter_text, reply_markup= starter_markup )

            case "edit":    
                # warning: upd.callback_query = None while starter by command(mode="new") which may lead to exception
                user_id = upd.callback_query.message.chat.id
                self.bot.edit_message_text( text= self.starter_text, chat_id=user_id, message_id= upd.callback_query.message.id, reply_markup= starter_markup )


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

                                            self.bot.edit_message_text( text= Tools().try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= range_keyb )           

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
                                                text= f"{Tools().try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data )}\nchosen year: {upd.callback_query.data.split('.')[8]}" , 
                                                chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, 
                                                reply_markup= None)   

                                            # append card value            


                                        case _:
                                            print( f"alarm:{len( upd.callback_query.data.split('.') )}" )    


                                case "array":

                                    inline = types.InlineKeyboardMarkup()

                                    for option in prop["options"]:                                                                                      #FIXME: ↓ unreliable (Am I meant key "label" is not stable ?)
                                        inline.add( types.InlineKeyboardButton( text=  Tools().try_str( lang_strings, f'{prop["id"]}.{option["id"]}', default= f"""{option["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ option['id'] }""" ) )

                                    inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
                                    self.bot.edit_message_text( text= Tools().try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



                                case "value":

                                    inline = types.InlineKeyboardMarkup()

                                    for option in prop["options"]:                                                                                      #FIXME: ↓ unreliable
                                        inline.add( types.InlineKeyboardButton( text=  Tools().try_str( lang_strings, f'{prop["id"]}.{option["id"]}', default= f"""{option["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ option['id'] }""" ) )

                                    inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
                                    self.bot.edit_message_text( text= Tools().try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           


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

            pair.append( types.InlineKeyboardButton( text=  Tools().try_str( lang_strings, f'{prop["id"]}.{option["id"]}', default= f"""{option["label"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ option['id'] }""" ) )

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
        self.bot.edit_message_text( text= Tools().try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           


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
            

class Tools():

    def __init__(self):
        pass   

    def try_str( self, string_data, id, default ):

        try:
            assert string_data[id] != None 
            return string_data[id]
        except:
            return default 
        

    def write_log( self, text ):
        print(text)    


    def update_users( self, upd_source, token ):
            try:
                if upd_source != None :
                    with open( R"C:\Users\nikita\Desktop\save\users.json", "r", encoding="utf-8" ) as f: #FIXME: file is magic string
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
                self.write_log( f"failed writing source({upd_source}) to sources" )    


    def get_upd_type( self, upd, default=False):
                            
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
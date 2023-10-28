"""from telebot import types
from Strings_Data import strings_data as strings
from avassist_types import Tools"""



"""class newSearch():

    def __init__( self, bot ):
        self.bot = bot


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
                inline.add( types.InlineKeyboardButton( text=  Tools.try_str( lang_strings, str(gr_item["id"]), default= f"""{gr_item["id"]}""" )  , callback_data= f"""{ upd.callback_query.data }.{ gr_item['id'] }""" ) )

            inline.add( self.back_button( upd_data=upd.callback_query.data ) )  
            self.bot.edit_message_text( text= Tools.try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



    def provide_ns_menu( self, upd ):
        
        if  self.bot.users[str( upd.callback_query.message.chat.id )].open_new_search_card( message_id= upd.callback_query.message.id ) is True:
                                            
            self.menu_navigation( upd )       

        else:
            self.bot.bot.answer_callback_query( callback_query_id= upd.callback_query.id, text= "Access denied :/ jr idk",
                show_alert= False
            )"""
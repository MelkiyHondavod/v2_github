import datetime
#import telebot
import time
import json

#from telebot import types
from telebot.apihelper import ApiTelegramException
from requests.exceptions import ConnectionError, ReadTimeout
from json_healer import heal

#from userClass import User
import avassist_types 
from Strings_Data import strings_data as strings

#from newSearch_scripted import newSearch


def main():
    #bot = FiltersBot( bot_key= "6378927209:AAFN58sc6C5qyfsBJP1GJOp5ab8GWtheI6w")
    token = "6502695853:AAGIg5f867h7lW1HwYoT521XswWZUL0ouZM"
    bot = avassist_types.FiltersBot( bot_key= token )
    #new_search = newSearch()

    json_data = {
        "recent_id": 0
    }

    print("started")


    while True:

        updates = []

        # this block provide code reliability. "Save" from connection troubles 
        try:
            updates = bot.bot.get_updates( offset=json_data["recent_id"]+1 , timeout= None, allowed_updates= [ "message", "callback_query" ] )
            if updates != [] :
                print( "new" )
        except ConnectionError :
            avassist_types.Tools().write_log(f"No responce [{time.asctime()}]")
        except ReadTimeout :
            avassist_types.Tools().write_log(f"ReadTimeout [{time.asctime()}]")   
        except ApiTelegramException as ate:
            if str(ate.error_code) != '409':
                avassist_types.Tools().write_log(f"ApiTelegramException [{time.asctime()}]")  
            else:       
                avassist_types.Tools().write_log(f"ApiTelegramException 409") 
            #print( type(ate) ) 
            #print( ate.error_code )



        for upd in updates :
            print('got upd')

            upd_source = None

            try:
                upd_type = avassist_types.Tools().get_upd_type( upd, default="not define" )
            except:
                upd_type = None
                avassist_types.Tools().write_log( f"   Warning: can't define upd type. UPD:{str(upd)}" )


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
                                bot.users[ str( upd.message.chat.id ) ] = avassist_types.User( tg_usr= upd.message.chat )

                            bot.starter( upd )



                        case "/status":
                            bot.bot.send_message( upd.message.chat.id, "камплит фильтэрс тоже воркают" )    

                        case _:
                            print( f"unknown command: {upd.message.text}" )    



                
                case "callback_query":
                    upd_source = str(upd.callback_query.message.chat.id)

                    #FIXME: dont forget to delete it on release
                    try:
                        bot.bot.answer_callback_query( callback_query_id= upd.callback_query.id, 
                                                      text= upd.callback_query.data,
                                                    show_alert= False
                                                )
                    except :
                        avassist_types.Tools().write_log( f"trouble with callback" ) 

                    match upd.callback_query.data.split('.')[0] :
                        
                        case "start":

                            if len(upd.callback_query.data.split('.')) > 1 :
                            
                                match upd.callback_query.data.split('.')[1] :

                                    case "new_search":
                                        #new search to user                       
                                        bot.provide_ns_menu( upd )      


                                    case _:
                                        avassist_types.Tools().write_log( f"unknown callback: {upd.callback_query.data}" )
                                        bot.bot.send_message( chat_id=upd.callback_query.message.chat.id, text=f"unknown callback: {upd.callback_query.data}" )

                            # why?    
                            else:
                                    bot.starter( upd=upd, mode = "edit" )   
                          


                        case _:
                            avassist_types.Tools().write_log( f"unknown callback: {upd.callback_query.data}" )
                            bot.bot.send_message( chat_id=upd.callback_query.message.chat.id, text=f"unknown callback: {upd.callback_query.data}" )#FIXME: dry?
                
                
                
                
                
                case _:
                    pass

            #update_users
            avassist_types.Tools().update_users( upd_source= upd_source, token= token )



            json_data["recent_id"] = upd.update_id        


if __name__=="__main__":
    main()            
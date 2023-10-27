import datetime
import telebot

from telebot import types
from telebot.apihelper import ApiTelegramException
from requests.exceptions import ConnectionError, ReadTimeout




class mainBot():
    
    def __init__( self, bot_key ):
        self.bot = telebot.TeleBot( bot_key )

    """def cycle(self):

        try:
            updates = self.bot.get_updates( offset=json_data["recent_id"]+1 , timeout= None )
        except ConnectionError :
            write_log(f"No responce [{time.asctime()}]")
        except ReadTimeout :
            write_log(f"ReadTimeout [{time.asctime()}]")   
        except ApiTelegramException :
            write_log(f"ApiTelegramException [{time.asctime()}]")

        updates = []
        for upd in updates:"""

        

    def notify():
        pass

    def old_notify( self, adv ):
        model_name = ""
        try:
            for i in range(0,3):
                model_name += adv.json_data["properties"][i]["value"] + "  " ##FIXME: skiped json load?
        except:
            model_name += "Error 1"



        """str_data = f"NOTIFICATION: {model_name}  ({adv.url}) time={datetime.datetime.now().strftime(r'%H:%M %d.%m.%Y')}"

        with open( fR"{root_path}\notifications.txt", "a", encoding="utf-8" ) as f:
            f.write( str_data + "\n")
            f.close()"""
        try:
            self.send_message( f"New({adv.json_data['originalDaysOnSale']}): {model_name} ${adv.price.usd} ({adv.url}) time={datetime.datetime.now().strftime(r'%H:%M %d.%m.%Y')}" )
            return 0
        except:
            return 1
        

    def send_message( self, text, chat=931481755 ):
        self.bot.send_message( chat_id=chat, text=text )
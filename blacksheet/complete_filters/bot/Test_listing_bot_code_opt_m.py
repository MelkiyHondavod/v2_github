from telebot import types
import json
from Strings_Data import strings_data as strings



def try_str( string_data, id, default ):

    try:
        assert string_data[id] != None 
        return string_data[id]
    except:
        return default
        


def listing( lang_strings, prop, page ):

        keyb = []

        prop_options = []
        next_button = 0
        tg_inline_lim = 100
        control_buttons_number = 1 #back
        option_instead_prev_button = 0
        

        if page>0 :
                control_buttons_number += 1 #prev_page_button 
                option_instead_prev_button = 1 #on first page printed 98 instead of 97
                prev_button = 1
                keyb.append( [types.InlineKeyboardButton( text="prev", callback_data="prev" )] )  
        
        #control_buttons_number = 3
        cb_default = 3
        control_buttons_number = control_buttons_number
        if len( prop["options"][  option_instead_prev_button + page*(tg_inline_lim-cb_default)   ::] ) <= tg_inline_lim-control_buttons_number :

            prop_options = prop["options"][  option_instead_prev_button+ page*(tg_inline_lim-cb_default)   ::] 

        else:
            control_buttons_number += 1 # next page
            prop_options = prop["options"][  option_instead_prev_button + page*(tg_inline_lim-cb_default)   :  option_instead_prev_button+ (page+1)*(tg_inline_lim-control_buttons_number)  :]   
            next_button =  [types.InlineKeyboardButton( text="next", callback_data="next" )]
            print( f"280923: {0 + page*(tg_inline_lim-control_buttons_number)} - { option_instead_prev_button + (page+1)*(tg_inline_lim-control_buttons_number) }" ) #97
                


        
        pair = []
        row_wide = 2
        for option in prop_options:   

            pair.append( types.InlineKeyboardButton( text=  f"""{option["label"]}"""  , callback_data= f"""xxx.{ option['id'] }""" ) )

            if len( pair ) == row_wide:
                keyb.append( pair ) 
                pair = []

        if pair != []:
            keyb.append( pair )

        #<-
        #->

        if next_button != 0 :
            keyb.append( next_button )

        keyb.append( [types.InlineKeyboardButton( text="back", callback_data="back" )] )    

        return keyb
            
        inline = types.InlineKeyboardMarkup(keyb)

        inline.add( back_button( upd_data=upd.callback_query.data ) )  
        print( "check" )
        #bot.edit_message_text( text= try_str(  lang_strings, upd.callback_query.data.split('.')[-1], default=  upd.callback_query.data ) , chat_id=upd.callback_query.message.chat.id, message_id=upd.callback_query.message.message_id, reply_markup= inline )           



def main():

    listing_test_prop = {
        "options":[
             
        ]
    }

    for i in range( 2023, 1826, -1 ):
        listing_test_prop["options"].append( 
            {
                "id": i,
                "label": str(i)
            }
         )

    #print( listing(lang_strings= strings.ru, prop = listing_test_prop )) 

    for row in listing(lang_strings= strings.ru, prop = listing_test_prop, page= 3 ) :
        for el in row :
            print( el.text, end='  ' )
        print()



if __name__ == "__main__" :
    main()
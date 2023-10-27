from blacksheet.complete_filters.bot.bot_code_opt_m_DEV import FiltersBot

back_button = FiltersBot.back_button

print( "\"" + back_button( self=None, upd_data= "new_search" ).callback_data + "\"" )

print( "new_search".split('.')  )
ns_split = "new_search".split('.')

for i in ns_split[:-1:] :
    print(i)
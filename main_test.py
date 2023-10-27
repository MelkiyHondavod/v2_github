from mainClass import Search
from botClass import mainBot
import datetime
import time
from root import rootPath
root_path = rootPath().path



def test_log( str_data ):
    with open( fR"{root_path}\test_log.txt", "a", encoding="utf-8" ) as f:
        f.write( str(now.strftime(r"%H:%M %d.%m.%Y")) +": " + str_data + "\n" )
        f.close()  



def notify( adv ):

    model_name = ""
    try:
        for i in range(0,3):
            model_name += adv.json_data["properties"][i]["value"] + "  " #FIXME: skiped json load?
    except:
        model_name += "Error 1"



    str_data = f"NOTIFICATION({adv.json_data['originalDaysOnSale']}): {model_name}  ({adv.url}) time={datetime.datetime.now().strftime(r'%H:%M %d.%m.%Y')}"

    with open( fR"{root_path}\notifications.txt", "a", encoding="utf-8" ) as f:
        f.write( str_data + "\n")
        f.close()   
  






search_init_data_list = [
    
    {
        "brand":"BMW",
        "model":"3 серия",
        "gen":"E30"
    },

    {
        "brand":"Honda",
        "model":"Accord",
        "gen":"IV"
    }, 

    {
        "brand":"Honda",
        "model":"Accord",
        "gen":"V"
    }, 
    
    {
        "brand":"BMW",
        "model":"5 серия",
        "gen":"E34"
    },
    
    {
        "brand": 'Mercedes-Benz',
        "model": '190 (W201)'
    },
    
    {
        "brand":"Honda",
        "model":"Civic",
        "gen":"V"
    },    
    
    {
        "brand": 'Audi',
        "model": '80',
        "gen": 'B2 · Рестайлинг'
    }
]

searches =[]
for sd in search_init_data_list:
    searches.append( Search( sd ) )



bot = mainBot( "6378927209:AAFN58sc6C5qyfsBJP1GJOp5ab8GWtheI6w" )

print("started")
now = datetime.datetime.now()
print(now.strftime(r"%H:%M %d.%m.%Y"))

while True:
    print("new_cycle")

    try:
        for srch in searches:
            for new_adv in srch.get_new_adverts():
                print(type(new_adv))
                notify( new_adv )
                if bot.old_notify( new_adv ) != 0:
                    test_log( f"failed bot notify:{ str(new_adv.json_data) }" )

    except Exception as e :
        test_log( f"!Exception: {e}" )

    min_to_sleep = 3
    time.sleep( min_to_sleep*60 )    
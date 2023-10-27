class User():

    def __init__( self, tg_usr, lang="en" ):
        self.id = tg_usr.id
        #self.username = tg_usr.username # can be also chat 
        self.lang = lang
        self.subscriptions = []
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


subscription_example = {
    "models":[
        {
            "exclude":False,
            "brand":383,
            "model":391,
            "generation":810
        },
        {
            "exclude":True,
            "brand":1279,
            "model":5173
        }
        
    ],
    "straight_type":{
        "transmission_type":2
    },
    "range_type":{
        "year":{
            "min":1950,
            "max":2023
        },
        "price_usd":{
            "max":100_000
        }
    }    
}        

def compile_init_string( sub ):

    init_str = "https://cars.av.by/filter?"


    for c, model in enumerate( sub["models"] ):
        
        if model["exclude"]:
            init_str += f"&brands[{c}][exclude]=1"

        for pair in model.items():
            if pair[0] != "exclude" :
                init_str += f"&brands[{c}][{pair[0]}]={pair[1]}" 


    for straight_type in sub["straight_type"].items():
        init_str += f"&{straight_type[0]}={straight_type[1]}"    


    for range_type in sub["range_type"].items():
        for range_pair in range_type[1].items():
            init_str += f"&{range_type[0]}[{range_pair[0]}]={range_pair[1]}"



    return init_str            

def main():
    print( compile_init_string( sub= subscription_example ) )   
    print('huj')

if __name__ == "__main__" :
    main()
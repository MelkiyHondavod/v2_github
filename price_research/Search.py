import requests
import json

def get_init_string_BMG(): # BMG - brand model generation

    headers = {
        'authority': 'api.av.by',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://av.by',
        'referer': 'https://av.by/',
        'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
        'x-api-key': '5f76cde7ebefc9.04631320',
        'x-device-type': 'web.desktop',
        'x-user-group': 'ae78505b-e27a-42d1-8e11-413e700f4de5',
    }

    class PropertyId():
        def __init__(self, data):
            self.id = data["id"]
            self.label = data["label"]



    #brand
    """class Brand():
        def __init__(self, data):
            self.id = data["id"]
            self.label = data["label"]"""

    response = requests.get('https://api.av.by/home/filters/home/init', headers=headers)

    
    brands = []
    for brand_data in json.loads(response.text)["blocks"][0]["rows"][0]["propertyGroups"][0]["properties"][0]["value"][0][1]["options"] :
        brands.append( PropertyId( brand_data ) )

    for b in brands:
        print( b.label )

    valid_input = False
    while not valid_input:
        input_brand = input( "Brand:" )
        for i in brands:
            if input_brand == i.label :
                valid_input = True
                chosen_brand_id = i.id
                break



    #model
    print( input_brand )    

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
                            'value': chosen_brand_id,
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

    models = []
    for model_data in json.loads(requests.post('https://api.av.by/home/filters/home/update', headers=headers, json=json_data).text)["properties"][0]["value"][0][2]["options"] :
        models.append(  PropertyId( model_data )  )

    for m in models:
        print(m.label)

    valid_input = False
    while not valid_input:
        input_model = input( "Model:" )
        for i in models:
            if input_model == i.label :
                valid_input = True
                chosen_model_id = i.id
                break    


    #generation
    print( input_model )   

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
                            'value': chosen_brand_id,
                        },
                        {
                            'name': 'model',
                            'value': chosen_model_id,
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

    generations = []
    for gen_data in json.loads(requests.post('https://api.av.by/home/filters/home/update', headers=headers, json=json_data).text)["properties"][0]["value"][0][3]["options"] :
        generations.append(  PropertyId( gen_data )  )

    for g in generations:
        print(g.label)

    valid_input = False
    while not valid_input:
        input_gen = input( "Gen:" )
        for i in generations:
            if input_gen == i.label :
                valid_input = True
                chosen_gen_id = i.id
                break    

    print(f"{input_brand}({chosen_brand_id}) {input_model}({chosen_model_id}) {input_gen}({chosen_gen_id})")
    return f"brands[0][brand]={chosen_brand_id}&brands[0][generation]={chosen_gen_id}&brands[0][model]={chosen_brand_id}&price_currency=2"




def get_init_string( data ):
    """data = {
        "brand":BMW, #unskipable
        "model":M3,
        "gen":E30,
    }"""

    with open( 'ierarchy.json', 'r', encoding="utf-8" ) as f:
        ierarchy_data = json.load( f ) 

    init_string = f"brands[0][brand]={ ierarchy_data[  data['brand']  ]['id']  }"
    try:
        init_string += f"&brands[0][model]={ ierarchy_data[  data['brand']  ]['models'][  data['model']  ]['id']}"
        init_string += f"&brands[0][generation]={ ierarchy_data[  data['brand']  ]['models'][  data['model']  ]['gens'][  data['gen']  ]['id'] }"
    except KeyError as e:
        print(f"KeyError:{e}")

    return init_string + "&price_currency=2"





def main():
    #print( get_init_string_BMG() )
    print( get_init_string( {
        "brand": 'BMW',
        "model": '3 серия'
        #"gen": 'E30'
    } ))

if __name__ == "__main__" :
    main()    
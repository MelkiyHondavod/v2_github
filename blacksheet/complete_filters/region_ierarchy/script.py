import requests
import json

location_ierarchy = []

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
id_neq_intValue = 0

for region in json.loads( response.content )["blocks"][2]["rows"][2]["propertyGroups"][0]["properties"][0]["options"] :
    print(  f"""{region["label"]}({region["name"]}): {region["id"]}"""  )

    location_ierarchy.append(
        {
            "name": region["name"],
            "label":region["label"],
            "id":region["id"],
            "cities":[]
        }
    )
    
    if region["id"] != region["intValue"] :
        id_neq_intValue += 1

    json_data = {
        'properties': [
            {
                'name': 'price_currency',
                'value': 2,
            },
            {
                'name': 'place_region',
                'value': [
                    region["id"],
                ],
                'modified': True,
                'previousValue': None,
            },
        ],
    }

    response = requests.post('https://api.av.by/home/filters/home/update', headers=headers, json=json_data)

    for city in json.loads( response.content )["properties"][0]["options"] :
        print(  f"""    {city["label"]}({city["name"]}): {city["id"]}"""  )
        
        location_ierarchy[-1]["cities"].append(
            {
                "name": city["name"],
                "label":city["label"],
                "id":city["id"]
            }
        )
        
        
        if city["id"] != city["intValue"] :
            id_neq_intValue += 1

print(f"errors:{ id_neq_intValue }")     

with open("blacksheet\\complete_filters\\region_ierarchy\\region_ierarchy.json", "w", encoding="utf-8") as f:
    json.dump( location_ierarchy, f, indent=4, ensure_ascii=False )
    f.close()
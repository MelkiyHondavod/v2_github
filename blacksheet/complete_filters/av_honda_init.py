import requests
import json

headers = {
    'authority': 'api.av.by',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': 'https://cars.av.by',
    'referer': 'https://cars.av.by/',
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
                        'value': 383,
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

response = requests.post('https://api.av.by/offer-types/cars/filters/main/update', headers=headers, json=json_data)

# Note: json_data will not be serialized by requests
# exactly as it was in the original request.
#data = '{"properties":[{"modified":true,"name":"brands","property":6,"value":[[{"name":"brand","value":383,"modified":true,"previousValue":null}]]},{"name":"price_currency","value":2}]}'
#response = requests.post('https://api.av.by/offer-types/cars/filters/main/update', headers=headers, data=data)

with open( "blacksheet\\complete_filters\\av_honda_post.json", "w", encoding="utf-8" ) as f:
    json.dump(  json.loads( response.content ) , f, ensure_ascii= False, indent=4 )
    print("dumped")
    f.close()    
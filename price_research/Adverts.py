#from cUrl.get_cURL import get_json_by_cURL
import requests
import json


def get_adverts_jsons(  init_string = "brands[0][brand]=8&brands[0][generation]=4425&brands[0][model]=5863&price_currency=2"  ):

    headers = {
        'authority': 'api.av.by',
        'accept': '*/*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,pl;q=0.6',
        'content-type': 'application/json',
        'dnt': '1',
        'origin': 'https://cars.av.by',
        'referer': 'https://cars.av.by/',
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
    
    adverts_jsons = []
    
    page = 1
    pages_mount = -1
    link_url = -1

    while page<=pages_mount or pages_mount==-1:

        response = requests.get(
            f'https://api.av.by/offer-types/cars/filters/main/init?{ init_string }&page={ page }',
            headers=headers,
        )

        responce_json = json.loads( response.text ) 
        adverts_jsons.extend( responce_json["adverts"] )
        page += 1

        if pages_mount == -1:
            pages_mount = responce_json["pageCount"]

        if link_url == -1:
            link_url = responce_json['seo']['currentPage']['url']    

    return adverts_jsons, link_url        





class Price():
    def __init__(self, prices):
        self.usd = prices["usd"]
        self.byn = prices["byn"]




class Advertisment():

    def __init__(self, json_data):
        self.json_data = json_data #FIXME: useless actually
        self.id = json_data["id"]
        self.url = json_data["publicUrl"]
        self.year = json_data["year"]
        self.publishedAt = json_data["publishedAt"]
        self.price = Price( {
            "usd": json_data["price"]["usd"]["amount"],
            "byn": json_data["price"]["byn"]["amount"]
            } )



def get_adverts( init_string ):
    adverts_json, link_url = get_adverts_jsons(init_string) #FIXME: nothing taken, should take "search"    

    advertisments = []
    for adv_json in adverts_json :
        advertisments.append( Advertisment( adv_json ) )

    #return advertisments    
    return advertisments, link_url    


def main(  ):
    
    adverts_json, link_url = get_adverts_jsons(  ) #FIXME: nothing taken, should take "search"    

    advertisments = []
    for adv_json in adverts_json :
        advertisments.append( Advertisment( adv_json ) )
        print( advertisments[-1].price.usd )

    print( len(advertisments) )





if __name__=="__main__":
    main() 
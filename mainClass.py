import requests
import json
from root import rootPath


def log( text, file_path=fR"{rootPath().path}\log.txt" ):
    with open( file_path, "a", encoding="utf-8" ) as f:
        f.write( text )
        f.close()


class Price():
        def __init__(self, prices):
            self.usd = prices["usd"]
            self.byn = prices["byn"]




class Advertisment():

        json_data = None
        id = None
        url = None
        year = None
        publishedAt = None
        price = Price( {
                    "usd": None,
                    "byn": None
                    } )

        def __init__(self, json_data):
            if json_data != None :
                self.json_data = json_data #FIXME: useless actually
                self.id = json_data["id"]
                self.url = json_data["publicUrl"]
                self.year = json_data["year"]
                self.publishedAt = json_data["publishedAt"]
                self.price = Price( {
                    "usd": json_data["price"]["usd"]["amount"],
                    "byn": json_data["price"]["byn"]["amount"]
                    } )
            else:
                log("WARNING: empty 'Advertisment' initialization")    
            




class Search():

    search_data = None
    advertisments = None
    avby_link = None
    subscribed_users = []

    def get_init_string(self, data ):
        """data = {
            "brand":BMW, #unskipable
            "model":M3,
            "gen":E30,
        }"""

        with open( 'ierarchy.json', 'r', encoding="utf-8" ) as f:
            ierarchy_data = json.load( f )
            f.close()#new 

        init_string = f"brands[0][brand]={ ierarchy_data[  data['brand']  ]['id']  }"
        try:
            init_string += f"&brands[0][model]={ ierarchy_data[  data['brand']  ]['models'][  data['model']  ]['id']}"
            init_string += f"&brands[0][generation]={ ierarchy_data[  data['brand']  ]['models'][  data['model']  ]['gens'][  data['gen']  ]['id'] }"
        except KeyError as e:
            print(f"KeyError:{e}")

        return init_string + "&price_currency=2&sort=4"
    
    def get_adverts_jsons(self, init_string ):#(  init_string = "brands[0][brand]=8&brands[0][generation]=4425&brands[0][model]=5863&price_currency=2"  ):

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

        response.close()#FIXME:sure?
        return adverts_jsons, link_url        
    


    def get_adverts(self, init_string ):
        adverts_json, link_url = self.get_adverts_jsons(init_string) #FIXME: nothing taken, should take "search"    

        advertisments = []
        for adv_json in adverts_json :
            advertisments.append( Advertisment( adv_json ) )

        #return advertisments    
        return advertisments, link_url
    
    ###########################################################################################################################
    def __init__(self, search_data=None) -> None:
        if search_data != None :
            self.search_data = search_data
            self.subscribed_users = []
            self.advertisments, self.avby_link = self.get_adverts_by_sd( search_data )

    def get_adverts_by_sd(self, search_data ): 
        advs, link = self.get_adverts( init_string=self.get_init_string( search_data ) )       
        return advs, link
    
    def get_new_adverts( self ):
        search_data = self.search_data
        cur_adverts, link = self.get_adverts_by_sd( search_data=search_data )

        c=0
        while c<len( cur_adverts ) :
            for old_adv in self.advertisments :
                if cur_adverts[c].url == old_adv.url :
                    cur_adverts.pop( c )
                    c-=1
                    break
            c+=1  #ahahahahahahahahahahahaha

        #update adverts
        self.advertisments.extend( cur_adverts )

        # new adverts
        return cur_adverts 

     
             


    



def test():
    pass


def main():
    test()

if __name__=="__main__":
    main()
from Adverts import get_adverts
from Search import get_init_string

search_data = {
    "brand":"BMW",
    "model":"3 серия",
    "gen":"E30"
}
search_data = {
    "brand": 'Lada (ВАЗ)',
    "model": 'XRAY'
}

search_data = {
    "brand":"BMW",
    "model":"5 серия",
    "gen":"E34"
}

search_data = {
    "brand": 'Mercedes-Benz',
    "model": '190 (W201)'
}

search_data={
    "brand":"Honda",
    "model":"Civic",
    "gen":"V"
}

search_data = {
    "brand":"BMW",
    "model":"3 серия",
    "gen":"E90, E91, E92, E93"
}

#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
adverts, link_url = get_adverts(init_string="brands[0][brand]=8&brands[0][model]=5863&brands[0][generation]=4429&body_type[0]=2&price_currency=2")#(  init_string=get_init_string( search_data )  )

print(  len(  adverts  ) )
max_cost = adverts[0].price.usd
min_cost = max_cost

for a in adverts:
    if a.price.usd > max_cost :
        max_cost = a.price.usd
    elif a.price.usd < min_cost:
        min_cost = a.price.usd

print( f"{min_cost}$ - {max_cost}$" )

grouped_by_cost = []
scale = 1000
for i in range(0, max_cost//scale + 1 ):
    grouped_by_cost.append([])

for a in adverts:
    grouped_by_cost[ a.price.usd//scale ].append( a )

for c, line in enumerate( grouped_by_cost ):
    print( f"{scale*c/1000}K$-{scale*(c+1)/1000}K$  :", end='' )
    for a in line:
        print( f" {a.price.usd}$;", end='' )    
    print()   

print( f"link:{link_url}" )
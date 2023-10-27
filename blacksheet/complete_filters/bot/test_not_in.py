import random
import json

jd = {}
#upd_source = "931481755"
#token = "6502695853:AAGIg5f867h7lW1HwYoT521XswWZUL0ouZM"

sources = [ "931481755" ]
for i in range(0, 9):
    sources.append( random.randint( 10**9, (10**10)-1 ) )

tokens = []
for i in range(0, 3):
    str_key=""
    for c in range(0,4):
        str_key += chr( random.randint(97,122) ) 
    tokens.append( f"{random.randint( 10**6, (10**7)-1 )}:{str_key}" )


for usr in sources:
    for c in range(0, random.randint(1,4)):
        bot_token = random.choice( tokens )
        print( f"{usr} call {bot_token}" )


        upd_source = usr
        token = bot_token
        if upd_source != None :

                if not upd_source in jd.keys():
                    jd[upd_source] = [ ]

                if not token in jd[upd_source] :
                    """print( jd[upd_source] )
                    print( jd[upd_source].copy().append("lol") )
                    a=jd[upd_source].copy()
                    a.append("lol")
                    print(f"a={a}")
                    #jd[upd_source] = jd[upd_source].copy().append( token )"""
                    jd[upd_source].append( token )

                    #print( jd )
print( jd )

print( json.dumps( jd, indent=4 ) )
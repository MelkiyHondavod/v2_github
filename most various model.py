import json



def most_gens_in_model():

    with open( "ierarchy.json", 'r', encoding="utf-8" ) as f:
        json_data = json.load( f )
        f.close()

    most_various_model = {
        "model_name": [None],
        "gens_amount": 0
    }

    top_n = []
    n = 4
    for c in range( 0, n ):
        top_n.append( most_various_model.copy() )

   # models_mount = 0

    for brand in json_data.items() :
        brand_name = brand[0]
        brand_data = brand[1]
        for model in brand_data["models"].items() :
            #models_mount += 1
            model_name = model[0]
            model_data = model[1]
            gens_number = len( model_data["gens"].keys() )

            c = n-1
            while True: # (  c>=0  ) :# and  (  gens_number >= top_n[ c ]["gens_amount"]  ) :

                if  gens_number < top_n[ c ]["gens_amount"]  or  ( c == -1 ):
                    if c+1 < n :
                        top_n.insert( c+1, most_various_model.copy() )
                        top_n.pop(-1)
                        top_n[c+1]["model_name"] = [ f"{brand_name} {model_name}" ]
                        top_n[c+1]["gens_amount"] = gens_number
                    break


                elif gens_number == top_n[ c ]["gens_amount"] :
                    top_n[c]["model_name"].append( f"{brand_name} {model_name}" )
                    break

                elif  gens_number > top_n[ c ]["gens_amount"] :
                    c -= 1

                

                
                

            """
            if gens_number > most_various_model["gens_amount"] :
                most_various_model["model_name"] = [ f"{brand_name} {model_name}" ]
                most_various_model["gens_amount"] = gens_number

            elif gens_number == most_various_model["gens_amount"] :
                print( str(most_various_model["model_name"]) + " = " +  f"{brand_name} {model_name}" )
                most_various_model["model_name"].append( f"{brand_name} {model_name}" )
            """    

            
                




    #print( json.dumps( most_various_model, indent= 4, ensure_ascii= False ) )     
    #print( models_mount )            
    print( json.dumps( top_n, indent= 4, ensure_ascii= False ) )  






def main():
    most_gens_in_model()

if __name__=="__main__":
    main()
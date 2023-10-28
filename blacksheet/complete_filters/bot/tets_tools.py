from avassist_types import Tools

str_data = {
    "1":"ein",
    "2":"zwei",
    "3":"drei"
}


for c in range (1,5):
    
    print(  Tools.try_str( 
        string_data= str_data,
        id= str(c),
        default= str(c)
        )  
    )
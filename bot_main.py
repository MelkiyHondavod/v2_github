import time
import datetime
from botClass import mainBot
from root import rootPath
import json


mb = mainBot()
av_cycles_delay = 70 #seconds
bot_cycles_delay = 2 #seconds
av_time1 = time.time()
bot_time1 = av_time1
run = 1
rootData = rootPath()

with open( fR"{rootData.path}\{rootData.data_file}", "r", encoding="utf-8" ) as f:
    pd = json.load( f )
    f.close()

    

try:
    while run==1:

        if time.time() - av_time1 > av_cycles_delay :
            av_time1 = time.time()

            #av by cycles
            for srch in searches:
                for new_adv in srch.get_new_adverts():
                    mb.notify( new_adv )

        #bot cycle   
        if time.time() - bot_time1 > bot_cycles_delay :
            av_time1 = time.time() 

            mb.cycle()

finally:
    pass            
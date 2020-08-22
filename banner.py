#python 2.7.15

#python 3.7.1

import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

os.system("clear")
os.system("figlet Banner Basliyor")
print "[                    ] 0% "
time.sleep(2)
print "[=====               ] 25%"
time.sleep(1)
print "[==========          ] 50%"
time.sleep(3)
print "[===============     ] 75%"
time.sleep(1)
print "[====================] 100%"
time.sleep(2)

banner="""

_  ___  _   _   _  _
| |/ / || | | |_| || |  __  ____ _
| ' /| || |_| __| || |_ \ \/ / _` |
| . \|__   _| |_|__   _| >  < (_| |
|_|\_\  |_|  \__|  |_|(_)_/\_\__, |
                                |_|
   
"""

print (banner)

import random
import time
while(True):
    room_temp=random.uniform(20,45)
    room_humidity=random.uniform(40,90)
    if(room_temp>35 or room_humidity<45):
        print("Alarm ON...Temperature:",room_temp)
    else:
        print("Alarm OFF...Temperature:",room_temp)
    time.sleep(1)
    

from __future__ import print_function
from inputs import get_key
from yeelight import Bulb
from yeelight import discover_bulbs

#import inputs
import random



list_bulbs=discover_bulbs()

#for element in list_bulbs:
#    print(element)

while 1:
    events = get_key()
    for event in events:
                print(event.ev_type, event.code, event.state)

    #R=random.randint(0,255)
    #G=random.randint(0,255)
    #B=random.randint(0,255)

    #bulb = Bulb(list_bulbs[0]["ip"]) #Take the first bulb of the list
    #bulb.turn_on()
    #bulb.set_rgb(R,G,B)

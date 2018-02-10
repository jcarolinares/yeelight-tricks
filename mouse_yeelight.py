from __future__ import print_function
from inputs import get_mouse
from yeelight import Bulb
from yeelight import discover_bulbs

import random
import inputs
import time


def main():
    try:
        list_bulbs=discover_bulbs()

        #for element in list_bulbs:
        #    print(element)

        while 1:
            events = get_mouse()
            for event in events:
                if event.code=="BTN_LEFT" and event.state==1:
                    R=random.randint(0,255)
                    G=random.randint(0,255)
                    B=random.randint(0,255)

                    bulb = Bulb(list_bulbs[0]["ip"],effect="smooth", duration=250) #Take the first bulb of the list
                    bulb.turn_on()
                    bulb.set_rgb(R,G,B)
                #print(event.ev_type, event.code, event.state)
                #Key BTN_LEFT 1
    except Exception as e:
        print("Error-Waiting 5 seconds to retrieve connection")
        time.sleep(5)
        print("Trying again...")
        raise main()


if __name__ == "__main__":
    main()

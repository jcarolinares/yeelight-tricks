import Yeelight
from threading import Thread
from time import sleep


#Start Detection thread
try:
    detection_thread = Thread(target=Yeelight.bulbs_detection_loop)
    detection_thread.start()
    # give detection thread some time to collect bulb info
    sleep(0.5)
    Yeelight.display_bulbs()

    #Yeelight.toggle_bulb(1)
    #Yeelight.set_bright(1,100)#bright range 0-100

    Yeelight.set_color(1,[255,255,255])

    # user interaction end, tell detection thread to quit and wait
    Yeelight.RUNNING = False
    detection_thread.join()
    print("thread over")

except:
    # user interaction end, tell detection thread to quit and wait
    Yeelight.RUNNING = False
    detection_thread.join()
    print("thread over")

from yeelight import Bulb

from yeelight import discover_bulbs
print(discover_bulbs())

bulb = Bulb("192.168.178.66")
bulb.turn_on()
bulb.set_rgb(200,23,100)

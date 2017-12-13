"""Display handler: outputs current track information to a Display-o-Tron HAT.

Draws heavily on Pimoroni example code:
https://github.com/pimoroni/displayotron
"""

from time import sleep
import paho.mqtt.client as mqtt
import math
import dothat.backlight as backlight
import dothat.lcd as lcd

print("""
Monitoring MQTT channels for jukebox info

Press CTRL+C to exit.
""")

lcd.clear()
lcd.set_cursor_position(0, 1)
lcd.write(" Such Rainbow! ")
lcd.contrast(55)

x = 0

while True:
    x += 1

    backlight.sweep((x % 360) / 360.0)
    backlight.set_graph(abs(math.sin(x / 100.0)))
    time.sleep(0.01)
"""Multiple servo test.

Try driving multiple servos from a single Pi: see what happens.
Execute with:
GPIOZERO_PIN_FACTORY=pigpio PIGPIO_ADDR=127.0.0.1 python3 servo02.py
...to load the pigpio pin factory, which evidently handles PWM rather
better than the default (which tops out around 3 servos)
"""

from time import sleep
from gpiozero import Servo

# myservo = [Servo(27), Servo(22), Servo(10), Servo(11),
#            Servo(6), Servo(13), Servo(19), Servo(26),
#            Servo(21), Servo(20), Servo(16), Servo(12)]

myservo = [Servo(27), Servo(22), Servo(10), Servo(11),
           Servo(6), Servo(13), Servo(19), Servo(26)]

# myservo = [Servo(21), Servo(20), Servo(16), Servo(12)]

delay = 1

while True:
    print("Go!")
    for servo in myservo:
        servo.max()
    sleep(delay)

    print("Mid!")
    for servo in myservo:
        servo.mid()
    sleep(delay)

    print("Back!")
    for servo in myservo:
        servo.min()
    sleep(delay)
    

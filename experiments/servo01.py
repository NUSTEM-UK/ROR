from gpiozero import Servo
from time import sleep

servo00 = Servo(27)
servo01 = Servo(22)
servo02 = Servo(10)
servo03 = Servo(11)

delay = 1

while True:
    print("Go!")
    servo00.min()
    servo01.min()
    servo02.min()
    servo03.min()
    sleep(delay)
    print("Mid!")
    servo00.mid()
    servo01.mid()
    servo02.mid()
    servo03.mid()
    sleep(delay)
    print("Back!")
    servo00.max()
    servo01.max()
    servo02.max()
    servo03.max()
    sleep(delay)
    

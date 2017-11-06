""" Robot Orchestra controller
"""


import paho.mqtt.client as mqtt # requires `pip install paho-mqtt`
import time
from threading import Timer
import numpy as np

# Nasty global variables. I should probably refactor soon.
currentBeat = 0 # Keep track of which beat we're playing
tempo = 120
bpm = 60.0 / tempo
running = True

class RepeatedTimer(object):
    """Simple timer class, from StackExchange (obviously).

    Credit: user MestreLion, https://stackoverflow.com/questions/3393612
    """

    def __init__(self, interval, function, *args):
        """Initialize the timer object."""
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.is_running = False
        self.start()

    def _run(self):
        """Timer has been triggered: execute callback function."""
        self.is_running = False
        self.start()
        self.function(*self.args)

    def start(self):
        """Start the timer, if it's not already running."""
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        """Stop the timer."""
        self._timer.cancel()
        self.is_running = False


# We only need a few of the methods from the previous mod_orchestra, so we'll
# simply declare them directly here.

mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"

def message(topic, payload)
    """Abstract out MQTT connection.

    Since it has to be done for each message, wrap it in a function.
    """
    mqttc.connect(mqtt_server, 1883)
    mqttc.publish("orchestra/" + topic, payload)

def playset(beatset):
    """Sends the current beat to all 8 channels at once."""
    message("playset", beatset)


def playBeat():
    # I may be using `global` incorrectly, here
    global currentBeat

    # Make ourselves an empty array in which we'll hold this column of beats
    curState = np.array([0, 0, 0, 0, 0, 0, 0, 0])

    # Trellis stuff here needs stripping out
    target = buttonGrid[0, currentBeat]

    # Get current state of this column of buttons
    for row in range(8):
        curState[row] = trellis.isLED(buttonGrid[row, currentBeat])

    # Concatenate array into string, for MQTT sending
    # array2string adds square braces; slice to remove them.
    curStateString = np.array2string(curState, separator='')[1:-1]
    # print curStateString

    # Command the orchestra!
    playset(curStateString)
   
    # set up for next beat, looping when we reach the end.
    currentBeat += 1
    if currentBeat > 15:
        currentBeat = 0


# ...and now we can actually run some code.
print('Press Ctrl-C to quit.')

# Initialise the timer, which will trigger at a rate specified by the
# bpm setting (ie, tempo)
rt = RepeatedTimer(bpm, playBeat)

# Initialise the timer, which will trigger at a rate specified by the
# bpm setting (ie, tempo)
rt = RepeatedTimer(bpm, playBeat)

# The main loop now only needs to handle button presses.
try:
    while True:
        time.sleep(0.08)

        # If a button was just pressed or released...
        if trellis.readSwitches():
            # go through every button
            for i in range(numKeys):
                # if it was pressed...
                if trellis.justPressed(i):
                    print('Button: {0}'.format(i))
                    # Alternate the LED
                    if trellis.isLED(i):
                        trellis.clrLED(i)
                    else:
                        trellis.setLED(i)
            # Update Trellis display.
            # Disabled by default since this gets triggered by the
            # timer anyway, and too frequent writeDisplays tend to
            # send things a bit funky.
            # trellis.writeDisplay()
        if startStopButton.is_pressed:
            if running:
                # Stop playback!
                print('>>> STOP')
                rt.stop()
                running = False
            else:
                # Start playback!
                print('>>> START')
                rt.start()
                running = True
finally:
    rt.stop()

""" Robot Orchestra controller
"""


import paho.mqtt.client as mqtt # requires `pip install paho-mqtt`
from guizero import App, Waffle, Text, Box, PushButton
import time
from threading import Timer
import numpy as np

dimension = 20
padding = 20
spacing = 5
num_beats = 16
num_channels = 8

# Nasty global variables. I should probably refactor soon.
currentBeat = 0 # Keep track of which beat we're playing

# Set up tempo and beats per minute. These variables are named wrong way around. Oops.
tempo = 120
bpm = 60.0 / tempo

# Is the playback timer running? (hint: it will be, on program launch)
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


mqttc = mqtt.Client()
mqtt_server = "10.0.1.5"

def change_pixel(x, y):
    if beat_set.get_pixel(x, y) == 'white':
        beat_set.set_pixel(x, y, "red")
    else:
        beat_set.set_pixel(x, y, "white")


def message(topic, payload):
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
    curState = np.zeros(num_channels, dtype=np.int)

    # Get current state of this column of buttons
    for row in range(num_channels):
        if beat_set.get_pixel(currentBeat, row) == "white":
            curState[row] = 0
            beat_set.set_pixel(currentBeat, row, "blue")
        else:
            curState[row] = 1
            beat_set.set_pixel(currentBeat, row, "white")
    
    # Concatenate array into string, for MQTT sending
    # array2string adds square braces; slice to remove them.
    curStateString = np.array2string(curState, separator='')[1:-1]
        
    # Just output to console, for now
    print(currentBeat, curStateString)

    # Command the orchestra!
    playset(curStateString)
   
    # Return column to previous colour
    for row in range(num_channels):
        if curState[row] == 0:
            beat_set.set_pixel(currentBeat, row, "white")
        else:
            beat_set.set_pixel(currentBeat, row, "red")

    # set up for next beat, looping when we reach the end.
    currentBeat += 1
    if currentBeat > (num_beats - 1):
        currentBeat = 0


def do_nothing():
    """Example button callback"""
    print("Button pushed")
    return 0


def startStopButton():
    global running
    if running:
        # Stop playback!
        print('>>> STOP')
        rt.stop()
        buttonStartStop.set_text("START")
        running = False
    else:
        # Start playback!
        print('>>> START')
        rt.start()
        buttonStartStop.set_text("STOP")
        running = True


def fasterButton():
    global tempo, rt
    tempo += 5
    if tempo > 240:
        tempo = 240
    bpm = 60.0/tempo
    rt.stop()
    rt = RepeatedTimer(bpm, playBeat)
    textBpm.set(tempo)


def slowerButton():
    global tempo, rt
    tempo -= 5
    if tempo < 30:
        tempo = 30
    rt.stop()
    rt = RepeatedTimer(bpm, playBeat)
    textBpm.set(tempo)

# ...and now we can actually run some code.
print('Press Ctrl-C to quit.')

app = App("Robot Orchestra", height=(100 + padding + num_channels*(dimension+spacing)),
          width=(padding + num_beats*(dimension + spacing)), layout="auto")

beat_set = Waffle(app, height=num_channels, width=num_beats, dim=dimension,
                  pad=spacing, dotty=False, remember=True, command=change_pixel)

box = Box(app, layout="grid")
textBpmLabel = Text(box, text="bpm", grid=[0,1])
textBpm = Text(box, text="120", grid=[0,2])
buttonFaster = PushButton(box, command=fasterButton, text="Faster", grid=[0,3])
buttonSlower = PushButton(box, command=slowerButton, text="Slower", grid=[0,4])
buttonStartStop = PushButton(box, command=startStopButton, text="STOP", grid=[0,5])

try:
    # Initialise the timer, which will trigger at a rate specified by the
    # bpm setting (ie, tempo)
    rt = RepeatedTimer(bpm, playBeat)
    # Display the app window
    app.display()
finally:
    # Tear everything down that we've worked so hard to create
    rt.stop()
    app.destroy()
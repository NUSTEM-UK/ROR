# NB. needs to run under python3, which is a bit of a pain in VS Code.

from guizero import App, Waffle
import time
from threading import Timer
import numpy as np

def change_pixel(x, y):
    if beat_set.get_pixel(x, y) == 'white':
        beat_set.set_pixel(x, y, "red")
    else:
        beat_set.set_pixel(x, y, "white")

dimension = 20
padding = 20
spacing = 5
num_beats = 16
num_channels = 8

currentBeat = 0 # Keep track of which beat we're playing
tempo = 240
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

def playBeat():
    # I may be using 'global' incorrectly here
    global currentBeat

    # Make ourselves an empty array in which we'll hold this column of beats
    curState = np.zeros(num_channels, dtype=np.int)

    for row in range(num_channels):
        if beat_set.get_pixel(currentBeat, row) == "white":
            curState[row] = 0
        else:
            curState[row] = 1
    
    # Just output to console, for now
    print(currentBeat, curState)

    currentBeat += 1
    if currentBeat > (num_beats - 1):
        currentBeat = 0


app = App("Waffle!", height=(padding + num_channels*(dimension+spacing)), width=(padding + num_beats*(dimension + spacing)) )
# app = App("Robot Orchestra")

beat_set = Waffle(app, height=num_channels, width=num_beats, dim=dimension, pad=spacing, dotty=False, remember=True, command=change_pixel)

rt = RepeatedTimer(bpm, playBeat)
app.display()


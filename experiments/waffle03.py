# NB. needs to run under python3, which is a bit of a pain in VS Code.

from guizero import App, Waffle

def change_pixel(x, y):
    if big_waffle.get_pixel(x, y) == 'white':
        big_waffle.set_pixel(x, y, "red")
    else:
        big_waffle.set_pixel(x, y, "white")

dimension = 20
padding = 20
spacing = 5
num_beats = 16
num_channels = 8

app = App("Waffle!", height=(padding + num_channels*(dimension+spacing)), width=(padding + num_beats*(dimension + spacing)) )
# app = App("Robot Orchestra")

big_waffle = Waffle(app, height=num_channels, width=num_beats, dim=dimension, pad=spacing, dotty=False, remember=True, command=change_pixel)

app.display()
# Installed GUIzero on the Mac with:
# sudo pip3 install git+https://github.com/lawsie/guizero.git@version-0.4
# (to get the prerelease version with clickable waffle installed)

# ...that didn't work, so instead did
#   sudo pip3 install guizero
# ...then integrated this pull request by hand into
#   /usr/local/lib/python3.6/site-packages/guizero/Waffle.py
#   https://github.com/lawsie/guizero/pull/28/files

# ...which is horrid, but GUIzero 0.4 is in flux at time of writing. Ugh.

# NB. needs to run under python3, which is a bit of a pain in VS Code.


from guizero import App, Waffle

def change_pixel(x, y):
    if big_waffle.get_pixel(x, y) == 'white':
        big_waffle.set_pixel(x, y, "red")
    else:
        big_waffle.set_pixel(x, y, "white")


app = App("Waffle!", height=50*20, width=50*20)

big_waffle = Waffle(app, height=80, width=80, dim=10, pad=2, dotty=True, remember=True, command=change_pixel)
# big_waffle = Waffle(app, height=80, width=80, dim=10, pad=2, dotty=True, remember=True)

app.display()
# Installed GUIzero on the Mac with:
# sudo pip install git+https://github.com/lawsie/guizero.git@version-0.4
# (to get the prerelease version with clickable waffle installed)

# NB. needs to run under python3, which is a bit of a pain in VS Code.


from guizero import App, Waffle

app = App()
my_waffle = Waffle(app, remember=True)

my_waffle.set_pixel(2, 1, "red")

print(my_waffle.get_pixel(2, 1))

print(my_waffle.get_pixel(1, 1))

app.display()
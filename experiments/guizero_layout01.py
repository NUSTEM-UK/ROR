from guizero import App, Waffle, PushButton, Box

def do_nothing():
    print("Button was pressed")

app = App()

my_box = Box(app, layout="grid")
my_button = PushButton(my_box, text="Button 1", command=do_nothing, grid=[0,0])
my_button2 = PushButton(my_box, text="Button 2", command=do_nothing, grid=[1,0])

my_waffle = Waffle(app, height=8, width=16, remember=True)

my_waffle.set_pixel(2, 1, "red")
print(my_waffle.get_pixel(2,1))
print(my_waffle.get_pixel(1,1))

app.display()
'''controls the model to run the game'''
from tkinter import Button, Canvas

# import model to refer to functions that buttons call via command=...
import model
from hallow import Hallow

TICK = 0

# def reset_button(parent, **config):
#     return Button(parent, command=model.reset, **config)

def save_button(parent, **config):
    return Button(parent, command=model.save, **config)

def load_button(parent, **config):
    return Button(parent, command=model.load, **config)

def next_button(parent, **config):
    return Button(parent, command=model.next_floor, **config)

def previous_button(parent, **config):
    return Button(parent, command=model.previous_floor, **config)



def board_canvas(parent, **config):
    "create the game board canvas and binding hotkeys"
    global THE_CANVAS
    THE_CANVAS = Canvas(parent, **config)
    #THE_CANVAS.bind("<ButtonRelease>", lambda event : model.mouse_click(event.x,event.y))
    THE_CANVAS.master.bind('n', lambda event: model.next_floor())
    THE_CANVAS.master.bind('p', lambda event: model.previous_floor())
    THE_CANVAS.master.bind('h', lambda event: model.show_info())
    THE_CANVAS.master.bind('s', lambda event: model.save())
    THE_CANVAS.master.bind('l', lambda event: model.load())

    THE_CANVAS.master.bind('<Left>', lambda event: model.arrow_direction('left'))
    THE_CANVAS.master.bind('<Right>', lambda event: model.arrow_direction('right'))
    THE_CANVAS.master.bind('<Up>', lambda event: model.arrow_direction('up'))
    THE_CANVAS.master.bind('<Down>', lambda event: model.arrow_direction('down'))

    return THE_CANVAS




def repeater(root):
    "repeatly calling model to display all elements"
    global TICK
    TICK = not TICK
    model.display_all(TICK)
    root.after(200, repeater, root)

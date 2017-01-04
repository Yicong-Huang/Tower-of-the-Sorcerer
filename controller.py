'''controls the model to run the game'''

from tkinter import Button, Canvas


import model

TICK = 0


def board_canvas(parent, **config):
    "create the game board canvas and binding hotkeys"
    global THE_CANVAS
    THE_CANVAS = Canvas(parent, **config)

    THE_CANVAS.master.bind('n', lambda event: model.next_floor())
    THE_CANVAS.master.bind('p', lambda event: model.previous_floor())
    THE_CANVAS.master.bind('h', lambda event: model.show_info())
    THE_CANVAS.master.bind('s', lambda event: model.save())
    THE_CANVAS.master.bind('l', lambda event: model.load())

    THE_CANVAS.master.bind('q', lambda event: exit())

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

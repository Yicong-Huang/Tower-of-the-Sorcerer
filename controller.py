from tkinter import Button,Label,Canvas

# import model to refer to functions that buttons call via command=...
import model

tick = 0
 
def reset_button  (parent,**config):
    return Button(parent,command=model.reset,**config)
 
def save_button  (parent,**config):
    return Button(parent,command=model.save,**config)

def load_button  (parent,**config):
    return Button(parent,command=model.load,**config)
 
def next_button  (parent,**config):
    return Button(parent,command=model.next,**config)
 
def previous_button  (parent,**config):
    return Button(parent,command=model.previous,**config)
 
 
 
def board_canvas  (parent,**config):
    global the_canvas
    the_canvas = Canvas(parent,**config)
    the_canvas.bind("<ButtonRelease>", lambda event : model.mouse_click(event.x,event.y))
    the_canvas.master.bind('<Left>',  lambda event : model.arrow_direction('left'))
    the_canvas.master.bind('<Right>', lambda event : model.arrow_direction('right'))
    the_canvas.master.bind('<Up>',  lambda event : model.arrow_direction('up'))
    the_canvas.master.bind('<Down>', lambda event : model.arrow_direction('down'))
    return the_canvas




def repeater(root):
    global tick
    tick = not tick
    model.display_all(tick)  
    root.after(200,repeater,root)
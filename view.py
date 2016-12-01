from tkinter import *

from PIL import ImageTk,Image
from PIL.ImageTk import PhotoImage

# import controller to call/create widgets and position them in the view
import controller

from item import Item

# Construct a simple root window
root =Tk()
root.title("Tower of the Szombieerer")
root.geometry("640x400")



left_image=ImageTk.PhotoImage(Image.open('src/frame/left.png'))
mid_image=ImageTk.PhotoImage(Image.open('src/frame/mid.png'))
right_image=ImageTk.PhotoImage(Image.open('src/frame/right.png'))
main = controller.board_canvas(root,width=640,height=400)
main.grid(sticky=W+E+N+S)
main.create_image(62.5,200,image=left_image,tag='init')
main.create_image(320,200,image=mid_image,tag='init')
main.create_image(577.5,200,image=right_image,tag='init')
yellow_key_icon=ImageTk.PhotoImage(Image.open('src/frame/yellow_key_icon.png'))
blue_key_icon=ImageTk.PhotoImage(Image.open('src/frame/blue_key_icon.png'))
red_key_icon=ImageTk.PhotoImage(Image.open('src/frame/red_key_icon.png'))
main.create_image(540,155,image=yellow_key_icon)
main.create_image(540,175,image=blue_key_icon)
main.create_image(540,195,image=red_key_icon)

transmit_up_icon=ImageTk.PhotoImage(Image.open('src/item/hallow/transmit_up.png'))

transmit_down_icon=ImageTk.PhotoImage(Image.open('src/item/hallow/transmit_down.png'))


frame = Frame(root)

# Place buttons simply at the top
frame.grid(row=1,sticky=S+W+N+E)
controller.reset_button (frame,text="New Floor")     .pack(side=LEFT)
controller.save_button (frame,text="Save Floor")     .pack(side=LEFT)
controller.load_button (frame,text="Load Floor")     .pack(side=LEFT)

controller.next_button (frame,text="Next Floor")     .pack(side=LEFT)
controller.previous_button (frame,text="Previous Floor")     .pack(side=LEFT)


variable = StringVar(root)
variable.set("wall") # default value

w = OptionMenu(root, variable, 'bat','big_bat','big_slime','blue_blood','blue_door','blue_gem','blue_key','blue_wizard','downstairs','ghost_soldier','green_slime','iron_door','knight','lava','merchant','mid_soldier','pri_witch','pro_witch','red_blood','red_door','red_gem','red_key','red_slime','red_wizard','rock','sage','skeleton','skeleton_soldier','slime_man','soldier','swords_man','upstairs','vampire_bat','wall', 'yellow_door','yellow_key','zombie','zombie_soldier')
w.grid(row=2,columnspan=3)

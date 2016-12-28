'''Display the game board with Tkinter, setting frame and some image constants.'''
from tkinter import Tk, W, E, S, N

from PIL import ImageTk, Image

# import controller to call/create widgets and position them in the view
import controller

# Construct a simple WINDOW WINDOW
WINDOW = Tk()
WINDOW.title("Tower of the Sorcerer")
WINDOW.geometry("640x400")

LEFT_IMAGE = ImageTk.PhotoImage(Image.open('src/frame/left.png'))
MID_IMAGE = ImageTk.PhotoImage(Image.open('src/frame/mid.png'))
RIGHT_IMAGE = ImageTk.PhotoImage(Image.open('src/frame/right.png'))
MAIN = controller.board_canvas(WINDOW, width=640, height=400)
MAIN.grid(sticky=W+E+N+S)
MAIN.create_image(62.5, 200, image=LEFT_IMAGE, tag='init')
MAIN.create_image(320, 200, image=MID_IMAGE, tag='init')
MAIN.create_image(577.5, 200, image=RIGHT_IMAGE, tag='init')
YELLOW_KEY_ICON = ImageTk.PhotoImage(Image.open('src/frame/yellow_key_icon.png'))
BLUE_KEY_ICON = ImageTk.PhotoImage(Image.open('src/frame/blue_key_icon.png'))
RED_KEY_ICON = ImageTk.PhotoImage(Image.open('src/frame/red_key_icon.png'))
MAIN.create_image(540, 155, image=YELLOW_KEY_ICON)
MAIN.create_image(540, 175, image=BLUE_KEY_ICON)
MAIN.create_image(540, 195, image=RED_KEY_ICON)

TRANSMIT_UP_ICON = ImageTk.PhotoImage(Image.open('src/item/hallow/transmit_up.png'))

TRANSMIT_DOWN_ICON = ImageTk.PhotoImage(Image.open('src/item/hallow/transmit_down.png'))

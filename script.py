'''
Start the game, calling view(set the board)
and controller (outside game control)
'''
import view
import controller

controller.repeater(view.root)

view.root.mainloop()

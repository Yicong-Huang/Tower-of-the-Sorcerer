'''Start the game, calling view(set the board)
and controller (outside game control)'''

import controller
import view

controller.repeater(view.WINDOW)

view.WINDOW.mainloop()

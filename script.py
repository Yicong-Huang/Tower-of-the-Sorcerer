'''Start the game, calling view(set the board)
and controller (outside game control)'''


import view
from controller import repeater

repeater(view.WINDOW)
view.WINDOW.mainloop()

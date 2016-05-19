# spots_gui.py
#
# ICS 32 Winter 2013
# Code Example
#
# This module implements a tkinter-based GUI application called Spots.
# The application begins with a blank canvas.  Clicking on the canvas
# causes a yellow "spot" to be drawn on the canvas.  Clicking within an
# existing spot instead causes that spot to be removed.  The spots get
# larger or smaller as the window is resized; they always cover a
# constant percentage of the canvas' area.

import coordinate

import spots_engine
import tkinter

##        self.column = column
##        self.row = row
##        self._root_window = tkinter.Tk()
##        self._canvas = tkinter.Canvas(
##            master =self._root_window, width=50*self.column, height=50*self.row,
##            background='green')
##
##        self._canvas.pack(padx = 20, pady = 20)
##        for i in range(self.column+12):
##            self._canvas.create_line(0,0,50*(i+1),0, width = 5.0)
##            self._canvas.create_line(0,0,0,50*(i+1), width = 5.0)
##            for a in range(self.row+12):
##                self._canvas.create_rectangle(50*(i+a), 50*(i), 50*(i+a+1), 50*(i+a+1))
##                self._canvas.create_rectangle(50*(i), 50*(i+a), 50*(i+a+1), 50*(i+a+1))

class SpotsApplication:
    def __init__(self, state):
        self._state = state
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window, width = 500, height = 450,
            background = '#006000')

        
        self._canvas.grid(
            row = 0, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.E + tkinter.W)

##        self._canvas.pack(padx = 20, pady = 20)
        self._canvas.bind('<Configure>', self._on_canvas_resize)
        self._canvas.bind('<Button-1>', self._on_mouse_click)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self):
        self._root_window.mainloop()


    def _on_canvas_resize(self, event):
        # Whenever the Canvas' size changes, redraw all of the spots,
        # since their sizes have changed, too.
        self._redraw_spots()


    def _on_mouse_click(self, event):
        # When the canvas is clicked, tkinter generates an event.  Since
        # we've bound to this method to that event, this method will be
        # called whenever the canvas is clicked.  The event object passed
        # to this method will have two useful attributes:
        #
        # * event.x, which specifies the x-coordinate where the click
        #   occurred
        # * event.y, which specifies the y-coordinate where the click
        #   occurred
        #
        # tkinter is not aware of the concept of fractional coordinates.
        # It always returns absolute coordinates.  But that's okay,
        # because we can simply create a Coordinate object and let it
        # do the appropriate conversion for us.
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        click_coordinate = coordinate.from_absolute(
            event.x, event.y, width, height)

        # Ask the SpotsState object to handle the click, by either
        # adding or removing a spot.
        self._state.handle_click(click_coordinate)

        # Now that a spot has either been added or removed, redraw
        # the dots.
        self._redraw_spots()
        

    def _redraw_spots(self):
        # Delete and redraw all of the spots.  Since spots are represented
        # by Spot objects that contain a top-left and bottom-right
        # Coordinate object, we can simply ask these Coordinate objects
        # to return their absolute coordinate and use that to do the
        # drawing.
        self._canvas.delete(tkinter.ALL)

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        for spot in self._state.all_spots():
            tlx, tly = spot.top_left_coordinate().absolute(width, height)
            brx, bry = spot.bottom_right_coordinate().absolute(width, height)
            
            self._canvas.create_oval(
                tlx, tly, brx, bry,
                fill = 'yellow', outline = 'black')



if __name__ == '__main__':
    # Create a SpotsState object that will store the current state of the
    # Spots application as it runs.
    state = spots_engine.SpotsState()

    # Pass the SpotsState to a newly-created SpotsApplication and then
    # start the application.
    SpotsApplication(state).start()

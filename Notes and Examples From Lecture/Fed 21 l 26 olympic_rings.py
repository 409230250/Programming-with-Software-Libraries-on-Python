# olympic_rings.py
#
# ICS 32 Winter 2013
# Code Example
#
# Executing this module displays what we called the "Olympic Rings"
# application, which displays the Olympic rings on a "tkinter" canvas.
# Unlike our previous use of a canvas, however, this one gets larger
# or smaller automatically as the size of the window changes, and the
# image drawn on the canvas is resized accordingly.  Unfortunately,
# "tkinter" doesn't automate this process, so we have to do some work
# to make it happen, but it's not an overwhelming amount of work.
#
# As we'll see in a future code example, building the right tools ahead
# of time will simplify matters even further.  But first thing's first;
# let's understand the problem of resizing a canvas and conceptualize a
# solution to it, then we'll worry about writing it cleanly.

import tkinter


class OlympicsRingsApplication:
    def __init__(self):
        # We'll set up the window the same way we set up the previous
        # one.  To make it show up more clearly, though, we'll make
        # the background of our canvas green, so we can more easily see
        # which part of the window contains our canvas and which part
        # is empty.
        self._root_window = tkinter.Tk()

        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 500, height = 400,
            background = 'green')

        # We'll discuss layout more thoroughly in a future lecture and
        # code example.  For now, the idea of what's happening here is
        # this:
        #
        # * The canvas is in grid cell (0, 0), which is the only grid
        #   cell in our window.
        # * As the size of grid cell (0, 0) changes, the size of our
        #   canvas changes accordingly, because it's "stuck" to all
        #   four edges of the cell (north, south, west, and east).
        # * There are 50 pixels of padding (empty space) inside of the
        #   grid cell (0, 0) horizontally and vertically, with the canvas
        #   surrounding by the padding.
        # * As the size of the window changes, all of the added or removed
        #   space is added to (or taken from) the size of grid cell (0, 0).

        self._canvas.grid(
            row = 0, column = 0, padx = 50, pady = 50,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resize)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self):
        self._root_window.mainloop()


    # Because of the call we made to bind() in the __init__ method,
    # this method is called whenever the size of the canvas changes.
    # We respond by calling our own _redraw() method to redraw the
    # image, given the new size of the canvas.
    def _on_canvas_resize(self, event):
        self._redraw()


    def _redraw(self):
        # Remove all of the shapes currently in the canvas.  (For a fun
        # effect, comment this line out and re-run the program.  Why does
        # it behave differently?)
        self._canvas.delete(tkinter.ALL)

        # Find out how big the canvas is, in terms of pixels, now.
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        # Draw the rings.  We always want the size of the rings to be
        # in the same proportions as the size of the canvas, so we're
        # passing "fractional coordinates" instead of "absolute coordinates".
        # When we actually draw ovals on the canvas, we'll convert the
        # fractional coordinates (ranging from 0.0 to 1.0 in the x and y
        # directions) to absolute coordinates (in terms of pixels, with
        # the range changing as the size of the canvas changes).
        self._draw_ring(width, height, .05, .05, .32, .32)
        self._draw_ring(width, height, .32, .32, .64, .64)
        self._draw_ring(width, height, .69, .69, .96, .96)
        self._draw_ring(width, height, .19, .19, .46, .46)
        self._draw_ring(width, height, .51, .51, .78, .78)


    def _draw_ring(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        # Given the width and height of the canvas, along with fractional
        # coordinates representing the top-left and bottom-right points of
        # the bounding box around the oval we want to draw, draw the
        # corresponding oval.  We have to convert the coordinates from
        # fractional to absolute in order to draw the oval, since Canvas'
        # create_oval() method expects absolute (pixel) coordinates.  We
        # can do that by multiplying the fractional coordinate by the
        # width or height, respectively.
        self._canvas.create_oval(
            width * tl_fracx, height * tl_fracy,
            width * br_fracx, height * br_fracy,
            outline='black')



if __name__ == '__main__':
    app = OlympicsRingsApplication()
    app.start()



import tkinter
class BoardApplication:
    def __init__(self, column, row):
        self._root_window = tkinter.Tk()
        self.column = column
        self.row = row
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 50*column, height = 50*row,
            background = 'green')

        self._canvas.grid(
            row = 0, column = 0, padx = 50, pady = 50,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resize)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)


    def start(self):
        self._root_window.mainloop()

    def _on_canvas_resize(self, event):
        self._redraw()

    def _redraw(self):
        self._canvas.delete(tkinter.ALL)

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for i in range (self.column):
            for a in range(self.column):
                self._draw_grid(width, height,(50*(i))/(50*self.column),
                              (50*(i))/(50*self.column), (50*(i+a+1))/(50*self.column),
                                ((i+a+1)*50)/(50*self.column))
                
    def _draw_grid(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_rectangle(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy)

if __name__ == '__main__':
    app = BoardApplication(6,6)
    app.start()

















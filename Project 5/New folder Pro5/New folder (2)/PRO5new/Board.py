
import tkinter
class BoardApplication:
    def __init__(self, column, row):
        self._root_window = tkinter.Tk()
        self.column = column
        self.row = row
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 50*self.column, height = 50*self.row,
            background = 'gray')

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
##        c = int(self.column/2)
##        r = int(self.row/2)
##        self._canvas.create_oval(51*(c-1),51*(r-1),50*(c),50*(r),
##            outline='gray', fill = 'black')

        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        for i in range (self.column-1):
            for a in range(self.row-1):
##                self._draw_grid(width, height,1/self.column,0,1/self.column,1)
                self._draw_grid(width, height,1/(self.column/(i+1)),0,1/(self.column/(i+1)),1)
                self._draw_grid(width, height,0,1/(self.row/(a+1)),1,1/(self.row/(a+1)) )

##                self._draw_grid(width, height, 10, 10/(50*self.row), ((self.column)*50+10)/(50*self.column),((self.row)*50+10)/(50*self.row))

##                self._canvas.create_line((50*self.column)/(self.column/1),0,(50*self.column)/(self.column/1),50*self.row)
##                self._canvas.create_line((50*self.column)/(self.column/2),0,(50*self.column)/(self.column/2),50*self.row)
##                self._canvas.create_line((50*self.column)/(self.column/3),0,(50*self.column)/(self.column/3),50*self.row)
##                self._canvas.create_line((50*self.column)/(self.column/4),0,(50*self.column)/(self.column/4),50*self.row)
##                self._canvas.create_line((50*self.column)/(self.column/5),0,(50*self.column)/(self.column/5),50*self.row)
##                self._draw_grid(width, height,(self.column/(i+1),0,self.column/(i+1),1))
##                self._canvas.create_line(0,50,50*self.column,50)

##                self._draw_grid(width, height, 0,(50*self.row)/(self.row/(a+1)),(50*self.column),(50*self.row)/(self.row/(a+1)))

##                self._canvas.create_line((50*self.row)/(self.row/4),3,(50*self.row)/(self.row/4),50*self.row)

##                self._canvas.create_line(10+120,10,10+120,60*self.row-10)
##                self._canvas.create_line(10+180,10,10+180,60*self.row-10)
##                self._canvas.create_line(10+200,10,10+200,60*self.row-10)
                
##                self._draw_grid(width, height,(50*(i))/(50*self.column),
##                              (50*(i))/(50*self.row), (50*(i+a+1))/(50*self.column),
##                                ((i+a+1)*50)/(50*self.row))
                
    def _draw_grid(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_line(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy)

##    def _create_circle()
##        self._canvas.create_oval(
##            outline='black')


if __name__ == '__main__':
    app = BoardApplication(6,4)
    app.start()

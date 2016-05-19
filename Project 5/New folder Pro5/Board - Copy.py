

import tkinter
class BoardApplication:
    def __init__(self, column, row, top):
        self.column = column
        self.row = row
        self.top = top 
        self._root_window = tkinter.Tk()
        self._canvas = tkinter.Canvas(
            master = self._root_window,
            width = 50*self.column, height = 50*self.row,
            background = 'gray')

        self._canvas.grid(
            row = 0, column = 0, padx = 50, pady = 50,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resize)
        #
        self._canvas.bind('<Button-1>', self._on_mouse_click)
        #
        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)
####################
    def _on_mouse_click(self, event):    
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()

        h = 0
        v = 0
        print(event.x, event.y)
        if event.x >= ((self.column*50)/(self.column/1-1)) and event.x < (self.column*50)/(self.column/1):
            h = 0
        else:
            for i in range(self.column):
                if event.x >= ((self.column*50)/(self.column/(i+1))) and event.x < (self.column*50)/(self.column/(i+2)):
                    h = (i+1)
                    
        if event.y >= ((self.row*50)/(self.row/1-1)) and event.y < (self.row*50)/(self.row/1):
            v = 0
        else:
            for j in range(self.row):
                if event.y >= ((self.row*50)/(self.row/(j+1))) and event.y < (self.row*50)/(self.row/(j+2)):
                    v = (j+1)

        tl_x = (h+0.04)/(self.column)
        tl_y = (v+0.04)/(self.row)
        br_x = (h+1-0.04)/(self.column)
        br_y = (v+1-0.04)/(self.row)
        self._draw_pieces(width, height, tl_x, tl_y, br_x, br_y)
        print([h+1,v+1])
        return([h+1,v+1])
    def _draw_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,
                                width * br_fracx, height * br_fracy, outline='white', fill = 'white')
####################
    def start(self):
        self._root_window.mainloop()

    def _on_canvas_resize(self, event):
        self._redraw()

    def _redraw(self):
        self._canvas.delete(tkinter.ALL)
        
##        self._create_pieces(width, height,(c)/self.column,(r)/self.row,(c+1)/self.column,(r+1)/self.row,
##            outline='gray', fill = 'black')
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        ##draw the grid
        for i in range (self.column-1):
            for a in range(self.row-1):
                self._draw_grid(width, height,1/(self.column/(i+1)),0,1/(self.column/(i+1)),1)
                self._draw_grid(width, height,0,1/(self.row/(a+1)),1,1/(self.row/(a+1)))
        
        c = int(self.column/2)
        r = int(self.row/2)
        if self.top == 'bw':
            ##create two black pieces
            self._black_pieces(width, height,((c-1)+0.04)/self.column,((r-1)+0.04)/self.row,(c-0.04)/self.column,(r-0.04)/self.row)
            self._black_pieces(width, height,(c+0.04)/self.column,(r+0.04)/self.row,(c+1-0.04)/self.column,(r+1-0.04)/self.row)
            ##create two white pieces
            self._white_pieces(width, height,((c-1)+0.04)/self.column,(r+0.04)/self.row,(c-0.04)/self.column,(r+1-0.04)/self.row)
            self._white_pieces(width, height,(c+0.04)/self.column,(r-1+0.04)/self.row,(c+1-0.04)/self.column,(r-0.04)/self.row)
        else:
            ##create two black pieces
            self._white_pieces(width, height,((c-1)+0.04)/self.column,((r-1)+0.04)/self.row,(c-0.04)/self.column,(r-0.04)/self.row)
            self._white_pieces(width, height,(c+0.04)/self.column,(r+0.04)/self.row,(c+1-0.04)/self.column,(r+1-0.04)/self.row)
            ##create two white pieces
            self._black_pieces(width, height,((c-1)+0.04)/self.column,(r+0.04)/self.row,(c-0.04)/self.column,(r+1-0.04)/self.row)
            self._black_pieces(width, height,(c+0.04)/self.column,(r-1+0.04)/self.row,(c+1-0.04)/self.column,(r-0.04)/self.row)

    def _draw_grid(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_line(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy)

    def _black_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy, outline='black', fill = 'black')
    def _white_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy, outline='white', fill = 'white')

if __name__ == '__main__':
    app = BoardApplication(16,4, 'bw')
    app.start()

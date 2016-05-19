
import inputs
import state
import tkinter

DEFAULT_FONT = ('Helvetica', 20)

class Application:
    def __init__(self):
        self._root_window = tkinter.Tk()

        self._board = None
        self._column = 0
        self._row = 0
        self._first_move = ''
        self._top_setting = ''
        self._how_to_win = ''

        Title = tkinter.Label(self._root_window, text = '',
            font = ('Helvetica', 5))
        Title.grid(row = 0, column = 0, columnspan = 2,
            sticky = tkinter.N)
        
        Title = tkinter.Label(self._root_window, text = 'Welcome To Reversi',
            font = DEFAULT_FONT)
        Title.grid(row = 1, column = 0, columnspan = 2,
            sticky = tkinter.N)
        
        start_button = tkinter.Button(self._root_window, text = 'Start',
            font = DEFAULT_FONT, command = self._on_start)
        start_button.grid(row = 2, column = 0, sticky = tkinter.N)

####################################
        self._message = tkinter.StringVar()
        self._message.set('No Message Yet!')

        message_label = tkinter.Label(
            self._root_window, textvariable = self._message,
            font = DEFAULT_FONT)
        message_label.grid(row = 3, column = 0, sticky = tkinter.S)

####################################      

        self._canvas = tkinter.Canvas(master = self._root_window,
            width = 600, height = 450,background = 'gray')
        self._canvas.grid(row = 4, column = 0, padx = 20, pady = 20,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._canvas.bind('<Configure>', self._on_canvas_resize)

        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.rowconfigure(2, weight = 1)
        self._root_window.rowconfigure(3, weight = 1)
        self._root_window.rowconfigure(4, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self):
        self._root_window.mainloop()
 
##    def _print_message(self):
##        if dialog.ok_clicked():
##            self._message.set('Invalid inputs')
            
    def _on_start(self):
        while True:
            dialog = inputs.APP()
            dialog.show()
            
            if dialog.ok_clicked():
                self._column = dialog.column_width()
                self._row = dialog.row_height()
                self._first_move = dialog.First_Move()
                self._top_setting = dialog.TopSetting()
                self._how_to_win = dialog.HowToWIN()

                connection = inputs.check_input([self._column, self._row, self._first_move, self._top_setting, self._how_to_win])
                if connection == False:
                    self._message.set('Invalid Inputs')
                    continue
                else:
                    self._column = connection[0]
                    self._row = connection[1]
                    self._first_move = connection[2]
                    self._top_setting = connection[3]
                    self._how_to_win = connection[4]
                    self._message.set('Good Inputs')
                    break
            elif dialog.cancel_clicked():
                self._message.set('Invalid Inputs')
                return None
                break
            
##            else:
##                pass
##            connection = inputs.check_input([self._column, self._row, self._first_move, self._top_setting, self._how_to_win])
##            if connection == False:
##                continue
##            else:
##                self._column = connection[0]
##                self._row = connection[1]
##                self._first_move = connection[2]
##                self._top_setting = connection[3]
##                self._how_to_win = connection[4]
##                break
        
        print(self._column, self._row, self._first_move, self._top_setting, self._how_to_win)

    
        self._board = state.makeNewBoard(self._row, self._column)
        state.get_board(self._board, self._row, self._column, self._top_setting)
        print(self._board)
        self._redraw()

    def _on_canvas_resize(self, event):
        self._redraw()
        
    def _redraw(self):
        self._canvas.delete(tkinter.ALL)
        
##        self._create_pieces(width, height,(c)/self.column,(r)/self.row,(c+1)/self.column,(r+1)/self.row,
##            outline='gray', fill = 'black')
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        ##draw the grid
        for i in range (self._column-1):
            for a in range(self._row-1):
                self._draw_grid(width, height,1/(self._column/(i+1)),0,1/(self._column/(i+1)),1)
                self._draw_grid(width, height,0,1/(self._row/(a+1)),1,1/(self._row/(a+1)))
        
        c = int(self._column/2)
        r = int(self._row/2)
##        if self._top_setting == 'bw':
##            ##create two black pieces
##            self._black_pieces(width, height,((c-1)+0.04)/self._column,((r-1)+0.04)/self.row,(c-0.04)/self._column,(r-0.04)/self._row)
##            self._black_pieces(width, height,(c+0.04)/self._column,(r+0.04)/self.row,(c+1-0.04)/self._column,(r+1-0.04)/self._row)
##            ##create two white pieces
##            self._white_pieces(width, height,((c-1)+0.04)/self._column,(r+0.04)/self.row,(c-0.04)/self._column,(r+1-0.04)/self._row)
##            self._white_pieces(width, height,(c+0.04)/self._column,(r-1+0.04)/self.row,(c+1-0.04)/self._column,(r-0.04)/self._row)
##        else:
##            ##create two black pieces
##            self._white_pieces(width, height,((c-1)+0.04)/self._column,((r-1)+0.04)/self._row,(c-0.04)/self._column,(r-0.04)/self._row)
##            self._white_pieces(width, height,(c+0.04)/self._column,(r+0.04)/self._row,(c+1-0.04)/self._column,(r+1-0.04)/self._row)
##            ##create two white pieces
##            self._black_pieces(width, height,((c-1)+0.04)/self._column,(r+0.04)/self._row,(c-0.04)/self._column,(r+1-0.04)/self._row)
##            self._black_pieces(width, height,(c+0.04)/self._column,(r-1+0.04)/self._row,(c+1-0.04)/self._column,(r-0.04)/self._row)

    def _draw_grid(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_line(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy)

    def _black_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy, outline='black', fill = 'black')
    def _white_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy, outline='white', fill = 'white')

if __name__ == '__main__':
    app = Application()
    app.start()

########################################################################################################################




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
##        print(event.x, event.y)
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
        print(h,v)
##        self._x = h+1
##        self._y = v+1
##        return([h+1,v+1])
##        Pass(h+1,v+1)._pass_xandy()

##    def _pass_xandy(self):
        
    
    


########check before draw out--------------------
##        tl_x = (h+0.04)/(self.column)
##        tl_y = (v+0.04)/(self.row)
##        br_x = (h+1-0.04)/(self.column)
##        br_y = (v+1-0.04)/(self.row)
####        print([h+1,v+1])
##        
##        self._draw_pieces(width, height, tl_x, tl_y, br_x, br_y)
##
##    def _draw_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
##        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,
##                                width * br_fracx, height * br_fracy, outline='white', fill = 'white')



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
    app = BoardApplication(14,4, 'wb')
    app.start()



    

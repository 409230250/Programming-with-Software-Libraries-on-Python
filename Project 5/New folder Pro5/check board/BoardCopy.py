import coordinate1
import inputs
import state_logic
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
        self._symbol = ''
        self._clicked_x = 0
        self._clicked_y = 0
        self._score1 = 0
        self._score2 = 0 

        Title = tkinter.Label(self._root_window, text = '',
            font = ('Helvetica', 5))
        Title.grid(row = 0, column = 0, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        Title = tkinter.Label(self._root_window, text = 'Welcome To Reversi',
            font = DEFAULT_FONT)
        Title.grid(row = 1, column = 0, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        start_button = tkinter.Button(self._root_window, text = 'Start',
            font = ('Helvetica', 15), command = self._click_start)
        start_button.grid(row = 2, column = 0,
                          sticky = tkinter.N + tkinter.S)

        self._message = tkinter.StringVar()
        self._message.set('No Message Yet!')

        message_label = tkinter.Label(
            self._root_window, textvariable = self._message, fg='red',
            font = DEFAULT_FONT)
        message_label.grid(row = 3, column = 0,
                           sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

##
        self._canvas = tkinter.Canvas(master = self._root_window,
            width = 600, height = 500,background = 'gray')
        self._canvas.grid(row = 5, column = 0, padx = 10, pady = 10,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._button_frame = tkinter.Frame(
            self._root_window)
        self._button_frame.grid(
            row=4, column=0, columnspan = 2,
            sticky = tkinter.N + tkinter.S )
        
        score1 = tkinter.Label(self._button_frame, text = '',
            font = ('Helvetica', 15))
        score1.grid(row = 0, column = 0, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        self._score1 = tkinter.StringVar()
        self._score1.set('')

        score1_label = tkinter.Label(
            self._button_frame, textvariable = self._score1,
            font = ('Helvetica', 15))
        score1_label.grid(row = 0, column = 3,
                          sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        score2 = tkinter.Label(self._button_frame, text = '',
            font = ('Helvetica', 15))
        score2.grid(row = 0, column = 5, columnspan = 2,
            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
        
        self._score2 = tkinter.StringVar()
        self._score2.set('')

        score2_label = tkinter.Label(
            self._button_frame, textvariable = self._score2,
            font = ('Helvetica', 15))
        score2_label.grid(row = 0, column = 7,
                          sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)
##

        self._root_window.rowconfigure(0, weight = 10)
        self._root_window.rowconfigure(1, weight = 10)
        self._root_window.rowconfigure(2, weight = 10)
        self._root_window.rowconfigure(3, weight = 10)
        self._root_window.rowconfigure(4, weight = 10)
        self._root_window.rowconfigure(5, weight = 10)
        self._root_window.columnconfigure(0, weight = 10)
        self._button_frame.rowconfigure(0, weight = 10)
        self._button_frame.rowconfigure(3, weight = 10)
        self._button_frame.rowconfigure(5, weight = 10)
        self._button_frame.rowconfigure(7, weight = 10)
        
################################################################
        self._canvas.bind('<Configure>', self._on_canvas_resize)
        self._canvas.bind('<Button-1>', self._on_mouse_click)
################################################################

    def _on_mouse_click(self, event):    
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        scores = state_logic.show_scores(self._board, self._row, self._column)

        if [self._column,self._row] == [0, 0]:
            return None
        elif (scores[0] + scores[1]) == (self._column*self._row):
            return None
        else:
            get_x, get_y = coordinate1.coor(self._column, self._row, event.x, event.y, width, height).calculate()
        if state_logic.MakeMove(self._board,'W', self._row, self._column).Flip_pieces() == []:
            if state_logic.MakeMove(self._board,'B', self._row, self._column).Flip_pieces() == []:
                return None
        if self._first_move == 'black':
            self._symbol = 'B'
            if state_logic.can_move(self._board, self._symbol, get_x, get_y, self._row, self._column) == False:
                self._message.set("Invalid move, black's turn")
                self._first_move = 'black'                

            else:
                state_logic.MakeMove(self._board, self._symbol, self._row, self._column).make_move_for_board(get_x, get_y)

                self._redraw()
                
                scores = state_logic.show_scores(self._board, self._row, self._column)
                self._score1.set('Black: {}'.format(scores[0]))
                self._score2.set('White: {}'.format(scores[1]))
                
                if state_logic.check_score(state_logic.show_scores(self._board, self._row, self._column)) != (self._row * self._column):  
                    if state_logic.MakeMove(self._board,'W', self._row, self._column).Flip_pieces() == []:
                        if state_logic.MakeMove(self._board,'B', self._row, self._column).Flip_pieces() == []:
                            self._message.set("White and black have no move.")
                            
                            if self._how_to_win == 'more':
                                if scores[0] > scores[1]:
                                    self._message.set('Black won the game!')
                                elif scores[0] < scores[1]:
                                    self._message.set('White won the game!')
                                else:
                                    self._message.set('This game is draw.')
                            else:
                                if scores[0] < scores[1]:
                                    self._message.set('Black won the game!')
                                elif scores[0] > scores[1]:
                                    self._message.set('White won the game!')
                                else:
                                    self._message.set('This game is draw.')
                                    
                            play_again_button = tkinter.Button(self._root_window, text = 'Play Again',
                                font = ('Helvetica', 15), command = self._click_start)
                            play_again_button.grid(row = 2, column = 0, sticky = tkinter.N)
                            
                        else:
                            self._message.set("White has no move; it's black turn!")
                            self._first_move = 'black'
                    
                    else:
                        self._first_move = 'white'
                        self._message.set("{}'s turn".format((self._first_move).capitalize()))
                else:
                    if self._how_to_win == 'more':
                        if scores[0] > scores[1]:
                            self._message.set('Black won the game!')
                        elif scores[0] < scores[1]:
                            self._message.set('White won the game!')
                        else:
                            self._message.set('This game is draw.')
                    else:
                        if scores[0] < scores[1]:
                            self._message.set('Black won the game!')
                        elif scores[0] > scores[1]:
                            self._message.set('White won the game!')
                        else:
                            self._message.set('This game is draw.')
                        
                    play_again_button = tkinter.Button(self._root_window, text = 'Play Again',
                        font = ('Helvetica', 15), command = self._click_start)
                    play_again_button.grid(row = 2, column = 0, sticky = tkinter.N)
                    
#White Turn                     
        elif self._first_move== 'white':
            
            self._symbol = 'W'
            if state_logic.can_move(self._board, self._symbol, get_x, get_y, self._row, self._column) == False:
                self._message.set("Invalid move, white's turn")
                self._first_move = 'white'
            else:
                state_logic.MakeMove(self._board, self._symbol, self._row, self._column).make_move_for_board(get_x, get_y)

                scores = state_logic.show_scores(self._board, self._row, self._column)
                self._score1.set('Black: {}'.format(scores[0]))
                self._score2.set('White: {}'.format(scores[1]))
                
                self._redraw()
                
                if state_logic.check_score(state_logic.show_scores(self._board, self._row, self._column)) != (self._row * self._column):
                    if state_logic.MakeMove(self._board,'B', self._row, self._column).Flip_pieces() == []:
                        if state_logic.MakeMove(self._board,'W', self._row, self._column).Flip_pieces() == []:
                            self._message.set("Black and white have no move.")

                            if self._how_to_win == 'more':
                                if scores[0] > scores[1]:
                                    self._message.set('Black won the game!')
                                elif scores[0] < scores[1]:
                                    self._message.set('White won the game!')
                                else:
                                    self._message.set('This game is draw.')
                            else:
                                if scores[0] < scores[1]:
                                    self._message.set('Black won the game!')
                                elif scores[0] > scores[1]:
                                    self._message.set('White won the game!')
                                else:
                                    self._message.set('This game is draw.')
                            play_again_button = tkinter.Button(self._root_window, text = 'Play Again',
                                font = ('Helvetica', 15), command = self._click_start)
                            play_again_button.grid(row = 2, column = 0, sticky = tkinter.N)
                            return None

                        else:
                            self._message.set("Black has no move; it's white turn!")
                            self._first_move = 'white'
                    else:
                        self._first_move = 'black'
                        self._message.set("{}'s turn".format((self._first_move).capitalize()))
                else:
                    scores = state_logic.show_scores(self._board, self._row, self._column)
                    if self._how_to_win == 'more':
                        if scores[0] > scores[1]:
                            self._message.set('Black won the game!')
                        elif scores[0] < scores[1]:
                            self._message.set('White won the game!')
                        else:
                            self._message.set('This game is draw.')
                    else:
                        if scores[0] < scores[1]:
                            self._message.set('Black won the game!')
                        elif scores[0] > scores[1]:
                            self._message.set('White won the game!')
                        else:
                            self._message.set('This game is draw.')
                        
                    play_again_button = tkinter.Button(self._root_window, text = 'Play Again',
                        font = ('Helvetica', 15), command = self._click_start)
                    play_again_button.grid(row = 2, column = 0, sticky = tkinter.N)
            
##        print(self._board,self._first_move)

    def start(self):
        self._root_window.mainloop()
        
    def _on_canvas_resize(self, event):
        self._redraw()
#            
    def _click_start(self):
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
                    self._message.set("{}'s turn".format((self._first_move).capitalize()))
                    break
            elif dialog.cancel_clicked():
                self._message.set('Canceled')
                return None
                break

##        print(self._column, self._row, self._first_move, self._top_setting, self._how_to_win)

        self._board = state_logic.makeNewBoard(self._row, self._column)
        state_logic.get_board(self._board, self._row, self._column, self._top_setting)
##        print(self._board,self._first_move)
        self._redraw()
        
    def _redraw(self):
        self._canvas.delete(tkinter.ALL)
        
        width = self._canvas.winfo_width()
        height = self._canvas.winfo_height()
        ##draw the grid
        for i in range (self._column-1):
            for a in range(self._row-1):
                self._draw_grid(width, height,1/(self._column/(i+1)),0,1/(self._column/(i+1)),1)  #V
                self._draw_grid(width, height,0,1/(self._row/(a+1)),1,1/(self._row/(a+1)))  #H
        ##The first 4 pieces
        c = int(self._column/2)
        r = int(self._row/2)
        for b in range(self._column):
            for c in range(self._row):
                if self._board[b][c] == 'W':
                    self._white_pieces(width, height,((b)+0.05)/self._column,((c)+0.05)/self._row,(b+1-0.05)/self._column,(c+1-0.05)/self._row)

                elif self._board[b][c] == 'B':
                    self._black_pieces(width, height,(b+0.05)/self._column,(c+0.05)/self._row,(b+1-0.05)/self._column,(c+1-0.05)/self._row)
 
    def _draw_grid(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_line(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy)

    def _black_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy, outline='black', fill = 'black')
    def _white_pieces(self, width, height, tl_fracx, tl_fracy, br_fracx, br_fracy):
        self._canvas.create_oval(width * tl_fracx, height * tl_fracy,width * br_fracx, height * br_fracy, outline='white', fill = 'white')


if __name__ == '__main__':
    app = Application()
    app.start()


import tkinter

DEFAULT_FONT = ('Helvetica', 20)

class NameDialog:
    def __init__(self):
        self._dialog_window = tkinter.Tk()

        who_label = tkinter.Label(
            self._dialog_window, text = 'How do you want to set up your board?',
            font = DEFAULT_FONT)
        who_label.grid(
            row = 0, column = 0,columnspan = 2,
            sticky = tkinter.W)
        
        self._column_label = tkinter.Label(
            self._dialog_window, text = 'Column of Size: ',
            font = DEFAULT_FONT)
        self._column_label.grid(row = 1, column = 0, sticky = tkinter.W)

        self._column_label_entry = tkinter.Entry(
            self._dialog_window, width = 20, font = DEFAULT_FONT)
        self._column_label_entry.grid(
            row = 1, column = 1,
            sticky = tkinter.W + tkinter.E)

        row_label = tkinter.Label(
            self._dialog_window, text = 'Row of Size: ',
            font = DEFAULT_FONT)
        row_label.grid(row = 2, column = 0, sticky = tkinter.W)

        self._row_label_entry = tkinter.Entry(
            self._dialog_window, width = 20, font = DEFAULT_FONT)
        self._row_label_entry.grid(
            row = 2, column = 1,
            sticky = tkinter.W + tkinter.E)
        
        who_go_first = tkinter.Label(
            self._dialog_window, text = 'Who Goes First: ',
            font = DEFAULT_FONT)
        who_go_first.grid(row = 3, column = 0, sticky = tkinter.W)

        who_go_first_frame = tkinter.Frame(self._dialog_window)
        who_go_first_frame.grid(row = 3, column = 1)

        black_button = tkinter.Button(
            who_go_first_frame, text = 'Black', font = DEFAULT_FONT,
            command = self._black_turn)
        black_button.grid(row = 0, column = 0)
        white_button = tkinter.Button(
            who_go_first_frame, text = 'White', font = DEFAULT_FONT)
##            command = )
        white_button.grid(row = 0, column = 1)


        wb_or_bw = tkinter.Label(
            self._dialog_window, text = 'WB_or_BW: ',
            font = DEFAULT_FONT)
        wb_or_bw.grid(row = 4, column = 0, sticky = tkinter.W)

        wb_or_bw_frame =  tkinter.Frame(self._dialog_window)
        wb_or_bw_frame.grid(row = 4, column = 1)
        WB_button = tkinter.Button(
            wb_or_bw_frame, text = 'WB', font = DEFAULT_FONT)
##command        
        WB_button.grid(row = 0, column = 0)
        BW_button = tkinter.Button(
            wb_or_bw_frame, text = 'BW', font = DEFAULT_FONT)
        #command
        BW_button.grid(row = 0, column = 1)        

        how_to_win = tkinter.Label(
            self._dialog_window, text = 'More/Less win: ',
            font = DEFAULT_FONT)
        how_to_win.grid(row = 5, column = 0, sticky = tkinter.W)

        how_to_win_frame = tkinter.Frame(self._dialog_window)
        how_to_win_frame.grid(row = 5, column = 1)
        more_button = tkinter.Button(
            how_to_win_frame, text = 'More', font = DEFAULT_FONT)
##            command = )
        more_button.grid(row = 0, column = 0)
        less_button = tkinter.Button(
            how_to_win_frame, text = 'Less', font = DEFAULT_FONT)
##            command = )
        less_button.grid(row = 0, column = 1)
########################################################################
        button_frame = tkinter.Frame(self._dialog_window)
        button_frame.grid(row = 6, column = 1, sticky = tkinter.E + tkinter.S)

        ok_button = tkinter.Button(
            button_frame, text = 'OK', font = DEFAULT_FONT,
            command = self._on_ok)
        ok_button.grid(row = 0, column = 0)

        cancel_button = tkinter.Button(
            button_frame, text = 'Cancel', font = DEFAULT_FONT,
            command = self._on_cancel)
        cancel_button.grid(row = 0, column = 1)

        QUIT_button = tkinter.Button(button_frame, text="QUIT", font = DEFAULT_FONT,
                                            command=self._dialog_window.destroy)
        QUIT_button.grid(row = 0, column = 2)
        
        self._dialog_window.columnconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(6,weight = 1)
        
        self._ok_clicked = False
        self._on_cancel = False
        self._column_label = ''
        self._row_label = ''
        self._who_go_first = ''
        self._wb_or_bw = ''
        self._how_to_win = ''
        
    def show(self):
        self._dialog_window.mainloop()
        
    def ok_clicked(self):
        return self._ok_clicked
    def column_name(self):
        return self._column_label
    def row_name(self):
        return self._row_label
    def who_go_first(self):
        return self._who_go_first
    def wb_or_bw(self):
        return self._wb_or_bw
    def howtowin(self):
        return self._how_to_win

    def _black_turn(self):
        return self._black_turn 


    def _on_ok(self):
        self._ok_clicked = True
        self._column_label = self._column_label_entry.get()
        self._row_label = self._row_label_entry.get()
        self._who_go_first = self._who_go_first_entry.get()
        self._wb_or_bw = self._wb_or_bw_entry.get()
        self._how_to_win = self._how_to_win_entry.get()
        self._dialog_window.destroy()

    def _on_cancel(self):
        self._on_cancel = True
        self._dialog_window.destroy()
        _on_greet()
      
##def connect(row, column, turn, top, win):
##    number = ['4','6','8', '10']
##    if not row in number:
##        print('Your column input is wrong')
##        return False
##    if not column in number:
##        print('Your row input is wrong')
##        return False
##    turn=''
##    if move_first == 'b':
##        turn = 'black'
##    elif move_first == 'w':
##        turn = 'white'
##    else:
##        print('Your first move input is wrong')
##        return False
##    if top != 'wb' and top != 'bw':
##        print('Your top input is wrong')
##        return False
##    if win != 'more' and win != 'less':
##        print('Your column input is wrong')
##        return False
    
def _on_greet():
    dialog = NameDialog()
    dialog.show()
    
    column = dialog.column_name()
    row = dialog.row_name()
    turn = dialog.who_go_first()
    top = dialog.wb_or_bw()
    win = dialog.howtowin()
##    if connect(row, column, turn, top, win) == False:
##        _on_greet()
    print (row, column, turn, top, win)
##        
_on_greet()

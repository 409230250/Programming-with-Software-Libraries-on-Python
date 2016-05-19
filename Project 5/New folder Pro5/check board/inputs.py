
import tkinter
class APP:
    def __init__(self):
        self._root_window = tkinter.Toplevel()

        subject = tkinter.Label(self._root_window, text = 'Set Up',
            font = ('Helvetica', 15))
        subject.grid(row = 0, column = 0)

        column_x = tkinter.Label(self._root_window, text = 'What size of column do you like?',
            font = ('Helvetica', 13))
        column_x.grid(row = 1, column = 0, sticky = tkinter.W)
        
        self.COLUMN= tkinter.IntVar()
        b1= tkinter.Radiobutton (self._root_window, text='4', value =4, variable = self.COLUMN)
        b1.grid(row = 1, column = 1, sticky = tkinter.W)
        b2= tkinter.Radiobutton (self._root_window, text='6', value =6, variable = self.COLUMN)
        b2.grid(row = 1, column = 2, sticky = tkinter.W)
        b3= tkinter.Radiobutton (self._root_window, text='8', value =8, variable = self.COLUMN)
        b3.grid(row = 1, column = 3, sticky = tkinter.W)
        b4= tkinter.Radiobutton (self._root_window, text='10', value =10, variable = self.COLUMN)
        b4.grid(row = 1, column = 4, sticky = tkinter.W)
        b5= tkinter.Radiobutton (self._root_window, text='12', value =12, variable = self.COLUMN)
        b5.grid(row = 1, column = 5, sticky = tkinter.W)
        b6= tkinter.Radiobutton (self._root_window, text='14', value =14, variable = self.COLUMN)
        b6.grid(row = 1, column = 6, sticky = tkinter.W)
        b7= tkinter.Radiobutton (self._root_window, text='16', value =16, variable = self.COLUMN)
        b7.grid(row = 1, column = 7, sticky = tkinter.W)

    ####################################################
        row_y = tkinter.Label(self._root_window, text = 'What size of row do you like?',
            font = ('Helvetica', 13))
        row_y.grid(row = 2, column = 0,sticky = tkinter.W)
        
        self.ROW= tkinter.IntVar()
        b8= tkinter.Radiobutton (self._root_window, text='4', value =4, variable = self.ROW)
        b8.grid(row = 2, column = 1, sticky = tkinter.W)
        b9= tkinter.Radiobutton (self._root_window, text='6', value =6, variable = self.ROW)
        b9.grid(row = 2, column = 2, sticky = tkinter.W)
        b10= tkinter.Radiobutton (self._root_window, text='8', value =8, variable = self.ROW)
        b10.grid(row = 2, column = 3, sticky = tkinter.W)
        b11= tkinter.Radiobutton (self._root_window, text='10', value =10, variable = self.ROW)
        b11.grid(row = 2, column = 4, sticky = tkinter.W)
        b12= tkinter.Radiobutton (self._root_window, text='12', value =12, variable = self.ROW)
        b12.grid(row = 2, column = 5, sticky = tkinter.W)
        b13= tkinter.Radiobutton (self._root_window, text='14', value =14, variable = self.ROW)
        b13.grid(row = 2, column = 6, sticky = tkinter.W)
        b14= tkinter.Radiobutton (self._root_window, text='16', value =16, variable = self.ROW)
        b14.grid(row = 2, column = 7, sticky = tkinter.W)

        who_goes_first = tkinter.Label(self._root_window, text = 'Who goes first?',
            font = ('Helvetica', 13))
        who_goes_first.grid(row = 3, column = 0, sticky = tkinter.W)
        
        self.first_move= tkinter.IntVar()
        b111= tkinter.Radiobutton (self._root_window, text='Black', value =1, variable = self.first_move)
        b111.grid(row = 4, column = 0, sticky = tkinter.W)
        b112= tkinter.Radiobutton (self._root_window, text='White', value =2, variable = self.first_move)
        b112.grid(row = 5, column = 0, sticky = tkinter.W)

        First4 = tkinter.Label(self._root_window, text = 'How to set the first 4 pieces?',
            font = ('Helvetica', 13))
        First4.grid(row = 6, column = 0,sticky = tkinter.W)

        self.top_set= tkinter.IntVar()
        b33= tkinter.Radiobutton (self._root_window, text='WB', value =1, variable = self.top_set)
        b33.grid(row = 7, column = 0, sticky = tkinter.W)
        b44= tkinter.Radiobutton (self._root_window, text='BW', value =2, variable = self.top_set)
        b44.grid(row = 8, column = 0, sticky = tkinter.W)

        How_to_win = tkinter.Label(self._root_window, text = 'How to win?',
            font = ('Helvetica', 13))
        How_to_win.grid(row = 9, column = 0,sticky = tkinter.W)

        self.set_win= tkinter.IntVar()
        b30= tkinter.Radiobutton (self._root_window, text='More', value =1, variable = self.set_win)
        b30.grid(row = 10, column = 0, sticky = tkinter.W)
        b40= tkinter.Radiobutton (self._root_window, text='Less', value =2, variable = self.set_win)
        b40.grid(row = 11, column = 0, sticky = tkinter.W)

        button_frame = tkinter.Frame(self._root_window)
        button_frame.grid(row = 12, column = 0, sticky = tkinter.E)

        ok_button = tkinter.Button(
            button_frame, text = 'OK', font = ('Helvetica', 20),
            command = self._on_ok)
        ok_button.grid(row = 0, column = 0)

        cancel_button = tkinter.Button(
            button_frame, text = 'Cancel', font = ('Helvetica', 20),
            command = self._on_cancel)

        cancel_button.grid(row = 0, column = 1)

        self._ok_clicked = False
        self._cancel_clicked = False
        self._column = 0
        self._row = 0
        self._first_move = ''
        self._top_setting = ''
        self._how_to_win = ''
        
    def show(self):
        self._root_window.grab_set()
        self._root_window.wait_window()
    def ok_clicked(self):
        return self._ok_clicked
    def cancel_clicked(self):
        return self._on_cancel
    def column_width(self):
        return self._column
    def row_height(self):
        return self._row
    def First_Move(self):
        return self._first_move
    def TopSetting(self):
        return self._top_setting
    def HowToWIN(self):
        return self._how_to_win
    
    def _on_ok(self):
        self._ok_clicked = True
        self._column = self.COLUMN.get()
        self._row = self.ROW.get()
        self._first_move = self.first_move.get()
        self._top_setting = self.top_set.get()
        self._how_to_win = self.set_win.get()
        self._root_window.destroy()
    def _on_cancel(self):
        self._cancel_clicked = True
        self._root_window.destroy()

    

##if __name__ == '__main__':
##    a = app()
##    a._root_window.mainloop()
##    print ([a.COLUMN.get(),a.ROW.get(),a.first_move.get(),a.top_set.get(),a.set_win.get()])

##print('this is what you pick: {}'.format(app.v.get()))




def check_input(information):
##    a = app()
##    a._root_window.mainloop()
##    information =([a.COLUMN.get(),a.ROW.get(),a.first_move.get(),a.top_set.get(),a.set_win.get()])
##    
    if information[0] in [4,6,8,10,12,14,16]:
        information[0] = information[0]

    if information[1] in [4,6,8,10,12,14,16]:
        information[1] = information[1]

    if information[2] == 1:
        information[2] = ('black')
    elif information[2] == 2:
        information[2] = ('white')

    if information[3] == 1:
        information[3] = 'wb'
    elif information[3] == 2:
        information[3] = 'bw'

    if information[4] == 1:
        information[4] = 'more'
    elif information[4] == 2:
        information[4] = 'less'

    if information[0]==0 or information[1]==0 or information[2] == 0 or information[3] ==0 or information[4] == 0:
        return False
    else:
        return (information)



##check_input()




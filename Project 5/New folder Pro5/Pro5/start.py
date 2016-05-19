import tkinter

DEFAULT_FONT = ('Helvetica', 20)

class NameDialog:
    def __init__(self):
        self._dialog_window = tkinter.Toplevel()

        who_label = tkinter.Label(
            self._dialog_window, text = 'How do you want to set up your board?',
            font = DEFAULT_FONT)
        who_label.grid(
            row = 0, column = 0, columnspan = 2,
            sticky = tkinter.W)
############################################
##column_label
##row_label
        
        column_label = tkinter.Label(
            self._dialog_window, text = 'Column of Size: ',
            font = DEFAULT_FONT)
        column_label.grid(row = 1, column = 0, sticky = tkinter.W)

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
        
########################################################################
        who_go_first = tkinter.Label(
            self._dialog_window, text = 'Who Go First: ',
            font = DEFAULT_FONT)
        who_go_first.grid(row = 3, column = 0, sticky = tkinter.W)

        self._who_go_first_entry = tkinter.Entry(
            self._dialog_window, width = 20, font = DEFAULT_FONT)
        self._who_go_first_entry.grid(
            row = 3, column = 1,
            sticky = tkinter.W + tkinter.E)

        wb_or_bw = tkinter.Label(
            self._dialog_window, text = 'WB_or_BW: ',
            font = DEFAULT_FONT)
        wb_or_bw.grid(row = 4, column = 0, sticky = tkinter.W)

        self._wb_or_bw_entry = tkinter.Entry(
            self._dialog_window, width = 20, font = DEFAULT_FONT)
        self._wb_or_bw_entry.grid(
            row = 4, column = 1,
            sticky = tkinter.W + tkinter.E)

        how_to_win = tkinter.Label(
            self._dialog_window, text = 'More/Less win: ',
            font = DEFAULT_FONT)
        how_to_win.grid(row = 5, column = 0, sticky = tkinter.W)

        self._how_to_win_entry = tkinter.Entry(
            self._dialog_window, width = 20, font = DEFAULT_FONT)
        self._how_to_win_entry.grid(
            row = 5, column = 1,
            sticky = tkinter.W + tkinter.E)
########################################################################
        button_frame = tkinter.Frame(self._dialog_window)
        button_frame.grid(row = 6, column = 1, sticky = tkinter.E + tkinter.S)
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

        self._dialog_window.columnconfigure(1, weight = 1)
        self._dialog_window.rowconfigure(0, weight = 1)
        self._dialog_window.rowconfigure(6,weight = 1)
        
        self._ok_clicked = False
        self._column_label = ''
        self._row_label = ''
        self._who_go_first = ''
        self._wb_or_bw = ''
        
    def show(self):
        self._dialog_window.grab_set()
        self._dialog_window.wait_window()
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
    def how_to_win(self):
        return self._how_to_win
    
    def _on_ok(self):
        self._ok_clicked = True
        self._column_label = self._column_label_entry.get()
        self._row_label = self._row_label_entry.get()
        self._who_go_first = self._who_go_first_entry.get()
        self._wb_or_bw = self._wb_or_bw_entry.get()
        self._how_to_win = self._how_to_win_entry.get()
        self._dialog_window.destroy()
    def _on_cancel(self):
        self._dialog_window.destroy()

class GreetingApplication:
    def __init__(self):
        self._root_window = tkinter.Tk()

        greet_button = tkinter.Button(
            self._root_window, text = 'Start',
            font = DEFAULT_FONT,
            command = self._on_greet)
        greet_button.grid(row = 0, column = 0)

        self._greeting = tkinter.StringVar()
        self._greeting.set('No Board Yet!')

        greeting_label = tkinter.Label(
            self._root_window, textvariable = self._greeting,
            font = DEFAULT_FONT)
        greeting_label.grid(row = 1, column = 0, sticky = tkinter.S)

        self._root_window.rowconfigure(0, weight = 1)
        self._root_window.rowconfigure(1, weight = 1)
        self._root_window.columnconfigure(0, weight = 1)

    def start(self):
        self._root_window.mainloop()
        
    def _on_greet(self):
        dialog = NameDialog()
        dialog.show()
        if dialog.ok_clicked():
            self._greeting.set(
                'The column number: {}\nThe row number: {}\nThe first move: {}\nThe top: {}\nThe decision of how to win: {}'.format(dialog.column_name(), dialog.row_name(),dialog.who_go_first(), dialog.wb_or_bw(),dialog.how_to_win()))

if __name__ == '__main__':
    application = GreetingApplication()
    application.start()

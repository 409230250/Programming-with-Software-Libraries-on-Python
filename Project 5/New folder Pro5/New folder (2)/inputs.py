
import tkinter
class app:
    r= tkinter.Tk()

    subject = tkinter.Label(r, text = 'Set Up',
        font = ('Helvetica', 15))
    subject.grid(row = 0, column = 0)

    column_x = tkinter.Label(r, text = 'What size of column do you like?',
        font = ('Helvetica', 13))
    column_x.grid(row = 1, column = 0, sticky = tkinter.W)
    
    COLUMN= tkinter.IntVar()
    b1= tkinter.Radiobutton (r, text='4', value =4, variable = COLUMN)
    b1.grid(row = 1, column = 1, sticky = tkinter.W)
    b2= tkinter.Radiobutton (r, text='6', value =6, variable = COLUMN)
    b2.grid(row = 1, column = 2, sticky = tkinter.W)
    b3= tkinter.Radiobutton (r, text='8', value =8, variable = COLUMN)
    b3.grid(row = 1, column = 3, sticky = tkinter.W)
    b4= tkinter.Radiobutton (r, text='10', value =10, variable = COLUMN)
    b4.grid(row = 1, column = 4, sticky = tkinter.W)
    b5= tkinter.Radiobutton (r, text='12', value =12, variable = COLUMN)
    b5.grid(row = 1, column = 5, sticky = tkinter.W)
    b6= tkinter.Radiobutton (r, text='14', value =14, variable = COLUMN)
    b6.grid(row = 1, column = 6, sticky = tkinter.W)
    b7= tkinter.Radiobutton (r, text='16', value =16, variable = COLUMN)
    b7.grid(row = 1, column = 7, sticky = tkinter.W)

####################################################
    row_y = tkinter.Label(r, text = 'What size of row do you like?',
        font = ('Helvetica', 13))
    row_y.grid(row = 2, column = 0,sticky = tkinter.W)
    
    ROW= tkinter.IntVar()
    b8= tkinter.Radiobutton (r, text='4', value =4, variable = ROW)
    b8.grid(row = 2, column = 1, sticky = tkinter.W)
    b9= tkinter.Radiobutton (r, text='6', value =6, variable = ROW)
    b9.grid(row = 2, column = 2, sticky = tkinter.W)
    b10= tkinter.Radiobutton (r, text='8', value =8, variable = ROW)
    b10.grid(row = 2, column = 3, sticky = tkinter.W)
    b11= tkinter.Radiobutton (r, text='10', value =10, variable = ROW)
    b11.grid(row = 2, column = 4, sticky = tkinter.W)
    b12= tkinter.Radiobutton (r, text='12', value =12, variable = ROW)
    b12.grid(row = 2, column = 5, sticky = tkinter.W)
    b13= tkinter.Radiobutton (r, text='14', value =14, variable = ROW)
    b13.grid(row = 2, column = 6, sticky = tkinter.W)
    b14= tkinter.Radiobutton (r, text='16', value =16, variable = ROW)
    b14.grid(row = 2, column = 7, sticky = tkinter.W)

    who_goes_first = tkinter.Label(r, text = 'Who goes first?',
        font = ('Helvetica', 13))
    who_goes_first.grid(row = 3, column = 0, sticky = tkinter.W)
    
    first_move= tkinter.IntVar()
    b111= tkinter.Radiobutton (r, text='Black', value =1, variable = first_move)
    b111.grid(row = 4, column = 0, sticky = tkinter.W)
    b112= tkinter.Radiobutton (r, text='White', value =2, variable = first_move)
    b112.grid(row = 5, column = 0, sticky = tkinter.W)

    First4 = tkinter.Label(r, text = 'How to set the first 4 pieces?',
        font = ('Helvetica', 13))
    First4.grid(row = 6, column = 0,sticky = tkinter.W)

    top_set= tkinter.IntVar()
    b33= tkinter.Radiobutton (r, text='WB', value =1, variable = top_set)
    b33.grid(row = 7, column = 0, sticky = tkinter.W)
    b44= tkinter.Radiobutton (r, text='BW', value =2, variable = top_set)
    b44.grid(row = 8, column = 0, sticky = tkinter.W)

    How_to_win = tkinter.Label(r, text = 'How to win?',
        font = ('Helvetica', 13))
    How_to_win.grid(row = 9, column = 0,sticky = tkinter.W)

    set_win= tkinter.IntVar()
    b30= tkinter.Radiobutton (r, text='More', value =1, variable = set_win)
    b30.grid(row = 10, column = 0, sticky = tkinter.W)
    b40= tkinter.Radiobutton (r, text='Less', value =2, variable = set_win)
    b40.grid(row = 11, column = 0, sticky = tkinter.W)

##if __name__ == '__main__':
##    app().r.mainloop()
##print('this is what you pick: {}'.format(app.v.get()))

##
def prin():
    app().r.mainloop()
    column = 0
    get_column = (app().COLUMN.get())
    if get_column in [4,6,8,10,12,14,16]:
        column = get_column
    else:
        print('No input for column.')

        
    row = 0    
    get_row = (app().ROW.get())
    if get_row in [4,6,8,10,12,14,16]:
        row = get_row
    else:
        print('No input for row.')

    first_turn = ''
    first = (app().first_move.get())
    if first == 1:
        first_turn = ('black')
    elif first == 2:
        first_turn = ('white')
    else:
        print('No input for the first move.')

    top = ''    
    top_set_up = (app().top_set.get())
    if top_set_up == 1:
        top = 'wb'
    elif top_set_up == 2:
        top = 'bw'
    else:
        print('No input for set up WB or BW.')

    win = ''
    howtowin = (app().set_win.get())
    if howtowin == 1:
        win = 'more'
    elif howtowin == 2:
        win = 'less'
    else:
        print('No input for how to win')

    if [column, row, first_turn, top, win] == [0,0,'','','']:
        print('No imput at all.')
    else:
        return ([column, row, first_turn, top, win])

      
##
##def check():
##    information = prin()
##    column = information[0]
##    row = information[1]
##    first_turn = information[2]
##    top = information[3]
##    win = information[4]
##    try:
##        if column == 0:
##            print('Check your last massegy and see which one you did not put input. And please try again.')
##            check()
##        elif row == 0:
##            print('Check your last massegy and see which one you did not put input. And please try again.')
##            check()
##        elif first_turn == '':
##            print('Check your last massegy and see which one you did not put input. And please try again.')
##            check()
##        elif top == '':
##            print('Check your last massegy and see which one you did not put input. And please try again.')
##            check()
##        elif win == '':
##            print('Check your last massegy and see which one you did not put input. And please try again.')
##            check()
##    except:
##        
##    else:
##        return [information[0],information[1],information[2],information[3],information[4]]
##check()
##






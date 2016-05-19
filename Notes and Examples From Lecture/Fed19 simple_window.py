# simple_window.py
#
# ICS 32 Winter 2013
# Code Example
#
# This example demonstrates a graphical user interface that contains only
# a single, large button.  The text of the button changes when the mouse
# moves inside of it.  Clicking the button causes a message to be printed
# to the console.

import tkinter



# In general, global variables are to be avoided in Python, except for
# global constants like these.  It's not a bad idea to move values like
# these into global constants, especially if they appear in more than one
# place in your code.
#
# I've declared these particular constants with names that begin with
# underscores, because they're private details of this module; we don't
# expect code outside of this module to care what text is inside the
# buttons or what message is printed to the console.

_NORMAL_BUTTON_TEXT = 'Hello Boo!'
_INSIDE_BUTTON_TEXT = 'Click Me!'
_BUTTON_CLICK_MESSAGE = 'Hello there, Boo Bear!'



def show_gui():
    # Create an empty window, into which we'll place widgets
    root_window = tkinter.Tk()

    # Create a button and place it into the window (that's what the
    # "master" option does).  We also set the text to be displayed in
    # the button (the "text" option), the font that the text should be
    # displayed with (the "font" option), and the command handler
    # function that should be called when the button is pressed
    # (the "command" option).  There are other options you can specify
    # on a button; they are listed exhaustively in the New Mexico Tech
    # Computer Center documentation on "tkinter".
    button = tkinter.Button(
        master=root_window, text=_NORMAL_BUTTON_TEXT,
        font=('Helvetica', 20), command=on_button_pressed)

    # Here, we're binding to two events on the button.  The first
    # parameter to each bind() call specifies the event that we're
    # interested in binding:
    #
    #     <Enter>, which means that the mouse cursor has entered the
    #              button's area
    #     <Leave>, which means that the mouse cursor has exited the
    #              button's area
    #
    # The second parameter to bind() is the event handler function
    # that will be called when the bound event occurs.  Event handler
    # functions take a single parameter, an event object that describes
    # the event that occurred.
    button.bind('<Enter>', on_mouse_entering_button)
    button.bind('<Leave>', on_mouse_leaving_button)

    # Since there's only one widget in our window, we can call pack()
    # on it to say "Whatever size this widget needs to be, resize the
    # window so it's that size, so that the widget fills the entire
    # available space in the window."
    button.pack()

    # Turn control over to "tkinter", who will run the show for us until
    # the window is closed.  Meanwhile, whenever an event occurs for which
    # we've registered interest -- the button is entered or exited, or
    # the button is clicked -- our code will be called.
    root_window.mainloop()



# Button command function that is called when the GUI's single button
# is clicked.  Button command functions take no parameters.  In our
# case here, that's no impediment, because we only plan to print a
# hard-coded message to the console.  In general, though, this is one of
# many reasons why using classes to implement GUIs makes a lot more sense,
# because we can use methods instead of functions to implement our command
# handlers and event handlers; since these methods will have a "self"
# parameter that will provide access to any attributes we store in our
# object, they will then have access to the information we need.
def on_button_pressed():
    print(_BUTTON_CLICK_MESSAGE)



# Event handler function that is called when the mouse cursor enters
# the GUI's single button.  Event handler functions take one parameter:
# an event object describing the event.  Event objects have different
# attributes depending on what kinds of events they are.  In this case,
# the only thing we care about is the "widget" attribute, which specifies
# the widget that the event affected.  That gives us the ability to get
# access to the button, so we can change its text.
def on_mouse_entering_button(event):
    # Widgets have what are called "options" (the things you set with
    # keyword arguments when you construct them).  A widget's options are
    # accessible by using the indexing operator on the widget, using the
    # name of the option as the index.  In this case, we want to set the
    # 'text' option (which specifies the text displayed in the button).
    event.widget['text'] = _INSIDE_BUTTON_TEXT



# Event handler function that is called when the mouse cursor exits the
# GUI's single button.
def on_mouse_leaving_button(event):
    event.widget['text'] = _NORMAL_BUTTON_TEXT



if __name__ == '__main__':
    # If we execute this module, we want to show the GUI.
    show_gui()

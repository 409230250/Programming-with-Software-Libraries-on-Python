##Junjie Lin 25792830 Project 5

## This module contains a Coordinate class. 

class coordinate:
    def __init__(self, column, row, event_x, event_y, width, height):
        self._column = column
        self._row = row
        if width == 0:
            self._x = event_x / (600)
        else:
            self._x = event_x / (width)

        if height == 0:
            self._y = event_y / (500)
        else:
            self._y = event_y / (height)
        self._clicked_x = 0
        self._clicked_y = 0

    def calculate(self):
        for i in range (self._column):
            if self._x >= 0 and self._x < (1/(self._column/(1))):
                self._clicked_x = 0
            else:
                if self._x >= (1/(self._column/(i+1))) and self._x < (1/(self._column/(i+2))):
                    self._clicked_x = i+1

        for a in range(self._row): 
            if self._y >= (0) and self._y < (1/(self._row/(1))):
                self._clicked_y = 0
            else:
                if self._y >= (1/(self._row/(a+1))) and self._y < (1/(self._row/(a+2))):
                    self._clicked_y = a+1
        return (self._clicked_x, self._clicked_y)


    

# coordinate.py
#
# ICS 32 Winter 2013
# Code Example
#
# This module contains a Coordinate class.  Objects of this class
# represent coordinates that can be translated between fractional
# and absolute coordinate systems; they are created using either a
# fractional or an absolute coordinate system, then can be asked to
# translate themselves to either system.
#
# The idea is that a coordinate in the fractional system corresponds
# naturally to a coordinate in the absolute system, and vice versa.
# So rather than spread the code that performs these conversions
# throughout our program, we're better off creating a tool to make
# this kind of conversion simpler.  We could manipulate text without
# string objects, but string objects make the job easier by providing
# a variety of useful methods like strip(), split(), and upper().
# Similarly, our Coordinate objects provide the raw materials to
# handle coordinate system conversions.

import math



# These two functions are used to create Coordinates that are either
# being created from fractional or absolute coordinates.  Given these
# two functions, we'll never create Coordinate objects by calling the
# Coordinate constructor; instead, we'll just call the appropriate
# of these two functions, depending on whether we have fractional or
# absolute coordinates already.

def from_frac(fracx, fracy):
    '''Builds a Coordinate given fractional x and y coordinates.'''
    return Coordinate(fracx, fracy, None, None, None, None)



def from_absolute(absx, absy, width, height):
    '''Builds a Coordinate given absolute x and y coordinates, along with
    the width and height of the absolute coordinate area (necessary for
    conversion to fractional).'''
    return Coordinate(None, None, absx, absy, width, height)



class Coordinate:
    def __init__(self, fracx, fracy, absx, absy, width, height):
        '''Initializes a Coordinate object.  The expectation is that either
        the fracx and fracy parameters *or* the absx, absy, width, and
        height parameters are specified, but not both.  Those that are not
        specified will have the value None.'''

        # Whether we're given fractional or absolute coordinates, we'll
        # store only the fractional x- and y-coordinates in attributes
        # of a Coordinate object.  The fractional x- and y-coordinates never
        # change for a particular Coordinate, but the absolute coordinates
        # may change depending on the width and height of the absolute
        # area.

        if fracx == None:
            # If absolute coordinates have been specified, convert them
            # to fractional using the provided width and height.
            self._fracx = absx / width
            self._fracy = absy / height
        else:
            # If fractional coordinates have been specified, store them
            # in attributes without conversion.
            self._fracx = fracx
            self._fracy = fracy


    def frac(self):
        '''Returns an (x, y) tuple that contains fractional coordinates
        for this Coordinate object.'''
        return self._fracx, self._fracy


    def absolute(self, width, height):
        '''Returns an (x, y) tuple that contains absolute coordinates for
        this Coordinate object.  The width and height are used to make
        the appropriate conversion -- absolute coordinates change as width
        and height changes.'''
        return self._fracx * width, self._fracy * height


    def frac_distance_from(self, other_coordinate):
        '''Given another Coordinate object, returns the distance, in
        terms of fractional coordinates, between this Coordinate and the
        other Coordinate.'''
        other_fracx, other_fracy = other_coordinate.frac()

        # Per the Pythagorean theorem from mathematics, the distance
        # between two coordinates is the square root of the sum of the
        # squares of the differences in the x- and y-coordinates.
        return math.sqrt(
            (self._fracx - other_fracx) ** 2 +
            (self._fracy - other_fracy) ** 2)

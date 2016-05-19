# example_indicators.py
#
# ICS 32 Winter 2013
# Code Example
#
# This module defines two classes, each of which specifies a kind of
# "indicator", in the spirit of the indicators from Project #3.  Each
# is implemented so that they have one method in common: an execute()
# method that takes a list of prices and returns a parallel list of
# indicator values for those prices.


class OddEvenIndicator:
    '''An odd/even indicator takes a list of prices and generates a parallel
    list of indicator values according to the following formula:
    * Take the price and turn it into an int (throwing away the cents)
    * See if the int(price) is an odd or an even number
    * If the price is odd, return +X
    * If the price is even, return -X
    * X is configurable by a user
    '''

    def __init__(self, x):
        '''Initializes an indicator by storing its X value'''
        self._x = x


    def x(self):
        '''Returns the X value associated with this indicator'''
        return self._x
    

    def execute(self, prices):
        '''Given a list of prices, execute this indicator and return a
        parallel list of indicator values'''
        indicators = []

        for price in prices:
            # By determining the integer version of each price and then
            # using the modulo (%) operator, we can determine whether each
            # price is an odd or even number of dollars.
            if int(price) % 2 == 1:
                indicators.append(self._x)
            else:
                indicators.append(self._x)

        return indicators





class ZeroIndicator:
    '''An indicator that always returns 0, regardless of what the given
    prices are'''

    def execute(self, prices):
        '''Given a list of prices, execute this indicator and return a
        parallel list of indicator values'''
        return [0] * len(prices)

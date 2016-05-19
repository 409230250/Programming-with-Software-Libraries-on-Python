# person.py
#
# ICS 32 Winter 2013
# Code Example
#
# This module defines a class called Person.  In this case, Person objects
# have the following abilities:
#
# * A Person object knows its first name
# * A Person object knows its last name
# * A Person object can tell you its first name
# * A Person object can tell you its last name
# * A Person object can tell you its full name, represented as its
#   first name, followed by a space, followed by the its last name
# * When you construct a Person object, you need to specify its
#   first name and last name, which are stored in the Person object
# * A Person's name cannot change
#
# To enforce the last requirement, we store the first and last name in
# private attributes (i.e., their names begin with underscores).


class Person:
    # Notice that our __init__ method has three parameters here.
    # However, the first one is "self", the parameter that indicates
    # what object the method was called on (in this case, what object
    # is being initialized).  Aside from "self", the method has two
    # additional parameters: both of these would need to be specified
    # if you wanted to construct a new Person.  So, for example, this
    # would be legal, in which case the newly-constructed Person would
    # be passed as self, 'Alex' would be passed as first_name,
    # and 'Thornton' would be passed as last_name.
    #
    #     p = Person('Alex', 'Thornton')
    #
    # but this would not be legal, because the two necessary parameters,
    # first_name and last_name, are missing:
    #
    #     p = Person()
    def __init__(self, first_name, last_name):
        '''Initializes this Person to have the given first name and
        last name'''
        self._first_name = first_name
        self._last_name = last_name


    def first_name(self):
        '''Returns the first name of this Person'''
        print (self._first_name)


    def last_name(self):
        '''Returns the last name of this Person'''
        return self._last_name


    def full_name(self):
        '''Returns the full name of this Person'''
        return self._first_name + ' ' + self._last_name

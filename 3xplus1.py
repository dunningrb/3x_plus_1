# -*- coding: utf-8 -*-
# 3x+1 problem
# Rodney Dunning

""" The 3x+1 Problem (also called the Collatz Problem) is an problem in number
    theory. To illustrate, pick any integer. If it is is even, divide by two. If
    it is odd, multiply by three and add one. Repeat this operation on the
    resulting integer. In this manner we build a chain of integer values.

    Example: 7. This number is odd, so multiply by three and add one to get 22.
    This number is even, so divide by two to get 11. We get the following chain:

    7 --> 22 --> 11 --> 34 --> 17 --> 52 --> 26 --> 13 --> 40 --> 20 --> 10 -->
    5 --> 16 --> 8 --> 4 --> 2 --> 1 --> 4 --> 2 --> 1 . . .

    Notice that by following the rules, the 4 --> 2 --> 1 sequence loops forever.

    Another example: 12.

    12 --> 6 --> 3 --> 10 --> 5 --> 16 -->8 --> 4 --> 2 --> 1 --> 4 --> 2 -->1

    We again reach the repeating 4 --> 2 --> 1 sequence. As far as we know ANY
    INTEGER you select as the starting point will eventually reach the 4 --> 2
    --> 1 loop. In other words, no other closed loops are known. The conjecture
    is that there are indeed no closed loops for any integer starting value.

    The 3x+1 Problem is to provide a formal proof that this result will hold for
    all integers. Proving this conjecture is an extraordinally difficult problem.

    This script illustrates the application of the two rules by constructing the
    integer chain for a given input value. The chain terminates at 1.


"""


class Collatz(object):

    """An object to build a "Collatz" chain.

    Attributes:
        x (int): The current value of the chain.

        finished (bol): Whether finished or not.

    """
    
    def __init__(self):

        """Initialize a Collatz object.

        """
        
        self.x = None
        self.finished = False

        while not self.finished: 
            self._get_starting_value()
            self._build_chain()
            self.finished = raw_input("Again? (y/n) ").lower() != "y"
        print "-----\n"

    def _end_chain(self):

        """Return a boolean.

        """
    
        return self.x == 1

    def _collatz_function(self):

        """Return x/2 for even x, 3x+1 for odd x.

        """
        
        mod = self.x%2
        return int(max(3*mod,0.5)*self.x + mod)

    def _get_starting_value(self):

        """Get an integer value from the user.

        """
        
        print "Please enter the starting value: "
        while type(self.x) is not int:
            try:        
                self.x = int((raw_input()))
            except ValueError:
                print "\nError. Please enter an integer value: "

    def _build_chain(self):

        """Build a Collatz chain of integer values.

        """
        
        while not self._end_chain():
            self.x = self._collatz_function()
            print "Next value is {0}".format(self.x)
        self.x = None
        print "Finished!!"


def main():
    Collatz()

if __name__ == "__main__":
    main()


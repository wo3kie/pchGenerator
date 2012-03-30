#
# Stack
#
class Stack:
    def __init__( self ):
        self.data = []

    def push( self, value ):
        self.data.append( value )

    def top( self ):
        if self.empty():
            raise Exception( "top on empty stack" )

        return self.data[-1]

    def pop( self ):
        if self.empty():
            raise Exception( "pop on empty stack" )

        return self.data.pop()

    def size( self ):
        return len( self.data )

    def empty( self ):
        return self.size() == 0

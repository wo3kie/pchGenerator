from stack import Stack

import unittest

#
# TestStack
#
class TestStack(unittest.TestCase):
    def test_negative( self ):
        stack = Stack()

        self.assertRaises( Exception, stack.top )
        self.assertRaises( Exception, stack.pop )

    def test_empty_size( self ):
        stack = Stack()

        self.assertTrue( stack.empty() )
        self.assertEqual( stack.size(), 0 )

        stack.push( 11 )
        self.assertFalse( stack.empty() )
        self.assertEqual( stack.size(), 1 )

    def test_push( self ):
        stack = Stack()

        stack.push( 11 )
        self.assertEqual( stack.top(), 11 )
        self.assertEqual( stack.size(), 1 )

        stack.push( 22 )
        self.assertEqual( stack.top(), 22 )
        self.assertEqual( stack.size(), 2 )

        stack.push( 33 )
        self.assertEqual( stack.top(), 33 )
        self.assertEqual( stack.size(), 3 )

    def test_pop( self ):
        stack = Stack()

        stack.push( 11 )
        stack.push( 22 )
        stack.push( 33 )

        self.assertEqual( stack.size(), 3 )
        self.assertEqual( stack.top(), 33 )
        self.assertEqual( stack.size(), 3 )
        self.assertEqual( stack.pop(), 33 )
        self.assertEqual( stack.size(), 2 )
        self.assertEqual( stack.top(), 22 )
        self.assertEqual( stack.size(), 2 )
        self.assertEqual( stack.pop(), 22 )
        self.assertEqual( stack.size(), 1 )
        self.assertEqual( stack.top(), 11 )
        self.assertEqual( stack.size(), 1 )
        self.assertEqual( stack.pop(), 11 )
        self.assertEqual( stack.size(), 0 )

#
# main
#
if __name__ == "__main__":
    unittest.main()

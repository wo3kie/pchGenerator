import unittest

from pch import\
    parseLine,\
    Stack

#
# TestParseLine
#
class TestParseLine( unittest.TestCase ):
    def test_negative( self ):
        self.assertRaises( Exception, parseLine, "line" )
        self.assertRaises( Exception, parseLine, ". " )
        self.assertRaises( Exception, parseLine, "...line" )
        self.assertRaises( Exception, parseLine, "......." )

    def test_positive( self ):
        self.assertEqual( parseLine( ". f" ), ( 1, "f" ) )
        self.assertEqual( parseLine( ".. directory" ), ( 2, "directory" ) )
        self.assertEqual( parseLine( "... path" ), ( 3, "path" ) )


#
# main
#
if __name__ == "__main__":
    unittest.main()
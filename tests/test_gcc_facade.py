import unittest

from gcc_facade import\
    GCCFacade

#
# TestGCCFacade
#
class TestGCCFacade( unittest.TestCase ):
    def test_negative( self ):
        gccFacade = GCCFacade()

        self.assertRaises( Exception, gccFacade.parseLine, "line" )
        self.assertRaises( Exception, gccFacade.parseLine, ". " )
        self.assertRaises( Exception, gccFacade.parseLine, "...line" )
        self.assertRaises( Exception, gccFacade.parseLine, "......." )

    def test_positive( self ):
        gccFacade = GCCFacade()

        self.assertEqual( gccFacade.parseLine( ". f" ), ( 1, "f" ) )
        self.assertEqual( gccFacade.parseLine( ".. directory" ), ( 2, "directory" ) )
        self.assertEqual( gccFacade.parseLine( "... path" ), ( 3, "path" ) )

#
# main
#
if __name__ == "__main__":
    unittest.main()
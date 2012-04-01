import unittest

from dag import\
    DagNode

from headers_dag import\
    HeaderNode,\
    HeadersDag

#
# TestDagNode
#
class TestDagNode( unittest.TestCase ):
    def test_init( self ):
        node = HeaderNode( "file.hpp" )

        self.assertEqual( node.getData(), "file.hpp" )
        self.assertEqual( len( node.getChildren() ), 0 )
        self.assertEqual( len( node.getParents() ), 0 )

        self.assertFalse( node.isIncluded() )
        self.assertEqual( node.getCounter(), 0 )

    def test_included( self ):
        node = HeaderNode( "file.hpp" )
        self.assertFalse( node.isIncluded() )

        node.setIncluded( True )
        self.assertTrue( node.isIncluded() )

        node.setIncluded( False )
        self.assertFalse( node.isIncluded() )

    def test_counter( self ):
        node = HeaderNode( "file.hpp" )
        self.assertEqual( node.getCounter(), 0 )

        node.setCounter( 1 )
        self.assertEqual( node.getCounter(), 1 )

        node.setCounter( 2 )
        self.assertEqual( node.getCounter(), 2 )

#
# TestDagHeaders
#
class TestDagHeaders( unittest.TestCase ):
    def test_processOneFile( self ):
        # . A
        # . B
        # . C

        headers = HeadersDag()

        nodeA = headers.add( 1, "A" )
        nodeB = headers.add( 1, "B" )
        nodeC = headers.add( 1, "C" )

        headers.processOneFile()

        self.assertFalse( nodeA.isIncluded() )
        self.assertFalse( nodeB.isIncluded() )
        self.assertFalse( nodeC.isIncluded() )

        self.assertTrue( nodeA.getCounter(), 1 )
        self.assertTrue( nodeB.getCounter(), 1 )
        self.assertTrue( nodeC.getCounter(), 1 )

        # . A  <
        # .. D <
        # . B  <
        # .. D <
        # . C

        nodeA = headers.add( 1, "A" )
        nodeD = headers.add( 2, "D" )
        nodeB = headers.add( 1, "B" )
        nodeD = headers.add( 2, "D" )

        headers.processOneFile()

        self.assertFalse( nodeA.isIncluded() )
        self.assertFalse( nodeB.isIncluded() )
        self.assertFalse( nodeC.isIncluded() )
        self.assertFalse( nodeD.isIncluded() )

        self.assertTrue( nodeA.getCounter(), 2 )
        self.assertTrue( nodeB.getCounter(), 2 )
        self.assertTrue( nodeC.getCounter(), 1 )
        self.assertTrue( nodeD.getCounter(), 1 )

#
# main
#
if __name__ == "__main__":
    unittest.main()

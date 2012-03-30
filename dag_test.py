import unittest

from dag import\
    Dag,\
    DagNode


#
# DagNode
#
class TestDagNode( unittest.TestCase ):
    def test_init( self ):
        node = DagNode( 11 )

        self.assertEqual( node.getData(), 11 )
        self.assertEqual( len( node.getChildren() ), 0 )
        self.assertEqual( len( node.getParents() ), 0 )

    def test_equal( self ):
        a11 = DagNode( 11 )
        b11 = DagNode( 11 )

        a22 = DagNode( 22 )
        b22 = DagNode( 22 )

        self.assertTrue( a11 == b11 )
        self.assertTrue( a22 == b22 )

        self.assertFalse( a11 == a22 )
        self.assertFalse( b11 == b22 )

    def test_addChild( self ):
        node1 = DagNode( 11 )
        node2 = DagNode( 22 )

        node1.addChild( node2 )
        self.assertTrue( node2 in node1.getChildren() )

        node2.addChild( node1 )
        self.assertTrue( node1 in node2.getChildren() )

    def test_addParent( self ):
        node1 = DagNode( 11 )
        node2 = DagNode( 22 )

        node1.addParent( node2 )
        self.assertTrue( node2 in node1.getParents() )

        node2.addParent( node1 )
        self.assertTrue( node1 in node2.getParents() )

#
# DAG
#
class DAGTest( unittest.TestCase ):
    def test_add_raise( self ):
        dag = Dag()

        self.assertRaises( Exception, dag.add, -1, "filename" )

        self.assertRaises( Exception, dag.add, 2, "filename" )
        self.assertRaises( Exception, dag.add, 3, "filename" )

        dag.add( 1, "filename" )

        self.assertRaises( Exception, dag.add, 3, "filename" )
        self.assertRaises( Exception, dag.add, 4, "filename" )

    def test_add_1( self ):
        dag = Dag()

         # filename_1_1
         #   filename_2_1
         #     filename_3_1
         #   filename_2_2
         #     filename_3_2
         # filename_1_2

        filename_1_1 = DagNode( "filename_1_1" )
        filename_2_1 = DagNode( "filename_2_1" )
        filename_3_1 = DagNode( "filename_3_1" )
        filename_2_2 = DagNode( "filename_2_2" )
        filename_3_2 = DagNode( "filename_3_2" )
        filename_1_2 = DagNode( "filename_1_2" )

        dag.add( 1, "filename_1_1" )
        dag.add( 2, "filename_2_1" )
        dag.add( 3, "filename_3_1" )
        dag.add( 2, "filename_2_2" )
        dag.add( 3, "filename_3_2" )
        dag.add( 1, "filename_1_2" )

        self.assertEqual( dag.getRoot().getChildren(), set( [ filename_1_1, filename_1_2 ] ) )

        self.assertEqual( dag.get( "filename_1_1" ).getChildren(), set( [ filename_2_1, filename_2_2 ] ) )
        self.assertEqual( dag.get( "filename_1_2" ).getChildren(), set() )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set( [ filename_3_1, ] ) )
        self.assertEqual( dag.get( "filename_2_2" ).getChildren(), set( [ filename_3_2, ] ) )

        self.assertEqual( dag.get( "filename_3_1" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_3_2" ).getChildren(), set() )

    def test_add_2( self ):
        dag = Dag()

         # filename_1_1
         #   filename_2_1
         #     filename_leaf
         # filename_leaf

        filename_1_1 = DagNode( "filename_1_1" )
        filename_2_1 = DagNode( "filename_2_1" )
        filename_leaf = DagNode( "filename_leaf" )

        dag.add( 1, "filename_1_1" )
        dag.add( 2, "filename_2_1" )
        dag.add( 3, "filename_leaf" )
        dag.add( 1, "filename_leaf" )

        self.assertEqual( dag.getRoot().getChildren(), set( [ filename_1_1, filename_leaf ] ) )

        self.assertEqual( dag.get( "filename_1_1" ).getChildren(), set( [ filename_2_1 ] ) )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set( [ filename_leaf, ] ) )

        self.assertEqual( dag.get( "filename_leaf" ).getChildren(), set() )

#
# main
#
if __name__ == "__main__":
    unittest.main()
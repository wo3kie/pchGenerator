import unittest

from dag import\
    DfsNode,\
    Dag,\
    DagNode

#
# TestDfsNode
#
class TestDfsNode( unittest.TestCase ):
    def test_init( self ):
        node = DfsNode()

        self.assertEqual( node.getColor(), DfsNode.White )
        self.assertEqual( node.getPreVisit(), -1 )
        self.assertEqual( node.getPostVisit(), -1 )

    def test_preVisit( self ):
        node = DfsNode()

        node.setPreVisit( 11 )
        self.assertEqual( node.getPreVisit(), 11 )

    def test_postVisit( self ):
        node = DfsNode()

        node.setPostVisit( 11 )
        self.assertEqual( node.getPostVisit(), 11 )

    def test_pre_post( self ):
        node = DfsNode()

        node.setPreVisit( 11 )
        node.setPostVisit( 22 )

        self.assertEqual( node.getPreVisit(), 11 )
        self.assertEqual( node.getPostVisit(), 22 )

    def test_pre_post_raise( self ):
        node = DfsNode()

        node.setPreVisit( 11 )
        self.assertRaises( Exception, node.setPostVisit, 10 )
        self.assertRaises( Exception, node.setPostVisit, 11 )

#
# TestDagNode
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

    def test_isRoot( self ):
        node1 = DagNode( 11 )
        node2 = DagNode( 22 )
        node3 = DagNode( 33 )

        self.assertTrue( node1.isRoot() )

        node1.addChild( node2 )
        self.assertTrue( node1.isRoot() )

        node3.addChild( node1 )
        self.assertTrue( node1.isRoot() )

        node1.addParent( node3 )
        self.assertFalse( node1.isRoot() )

    def test_isLeaf( self ):
        node1 = DagNode( 11 )
        node2 = DagNode( 22 )
        node3 = DagNode( 33 )

        self.assertTrue( node1.isLeaf() )
        self.assertTrue( node2.isLeaf() )
        self.assertTrue( node3.isLeaf() )

        node1.addChild( node2 )
        self.assertFalse( node1.isLeaf() )
        self.assertTrue( node2.isLeaf() )

        node3.addChild( node1 )
        self.assertFalse( node1.isLeaf() )

    def test_setColorRecursively( self ):
        node1 = DagNode( 11 )
        node2 = DagNode( 22 )
        node3 = DagNode( 33 )

        node1.addChild( node2 );
        node2.addChild( node3 );

        self.assertEqual( node1.getColor(), DfsNode.White )
        self.assertEqual( node2.getColor(), DfsNode.White )
        self.assertEqual( node3.getColor(), DfsNode.White )

        node1.setColorRecursively( DfsNode.Black )

        self.assertEqual( node1.getColor(), DfsNode.Black )
        self.assertEqual( node2.getColor(), DfsNode.Black )
        self.assertEqual( node3.getColor(), DfsNode.Black )
#
# DAGTest
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
        self.assertEqual( dag.get( "filename_1_1" ).getParents(), set( [ dag.getRoot() ] ) )

        self.assertEqual( dag.get( "filename_1_2" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_1_2" ).getParents(), set( [ dag.getRoot() ] ) )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set( [ filename_3_1, ] ) )
        self.assertEqual( dag.get( "filename_2_1" ).getParents(), set( [ dag.get( "filename_1_1" ) ] ) )

        self.assertEqual( dag.get( "filename_2_2" ).getChildren(), set( [ filename_3_2, ] ) )
        self.assertEqual( dag.get( "filename_2_2" ).getParents(), set( [ dag.get( "filename_1_1" ) ] ) )

        self.assertEqual( dag.get( "filename_3_1" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_3_1" ).getParents(), set( [ dag.get( "filename_2_1" ) ] ) )

        self.assertEqual( dag.get( "filename_3_2" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_3_2" ).getParents(), set( [ dag.get( "filename_2_2" ) ] ) )

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
        self.assertEqual( dag.get( "filename_1_1" ).getParents(), set( [ dag.getRoot() ] ) )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set( [ filename_leaf, ] ) )
        self.assertEqual( dag.get( "filename_2_1" ).getParents(), set( [ filename_1_1 ] ) )

        self.assertEqual( dag.get( "filename_leaf" ).getChildren(), set() )
        self.assertEqual( \
            dag.get( "filename_leaf" ).getParents()\
            , set( [ filename_2_1, dag.getRoot() ] )\
        )

    def test_add_3( self ):
        dag = Dag()

         # filename_1_1
         #   filename_2_1
         #     filename_3_1
         #   filename_2_2
         #     filename_3_1


        filename_1_1 = DagNode( "filename_1_1" )
        filename_2_1 = DagNode( "filename_2_1" )
        filename_3_1 = DagNode( "filename_3_1" )
        filename_2_2 = DagNode( "filename_2_2" )

        dag.add( 1, "filename_1_1" )
        dag.add( 2, "filename_2_1" )
        dag.add( 3, "filename_3_1" )
        dag.add( 2, "filename_2_2" )
        dag.add( 3, "filename_3_1" )

        self.assertEqual( dag.getRoot().getChildren(), set( [ filename_1_1 ] ) )

        self.assertEqual( dag.get( "filename_1_1" ).getChildren(), set( [ filename_2_1, filename_2_2 ] ) )
        self.assertEqual( dag.get( "filename_1_1" ).getParents(), set( [ dag.getRoot() ] ) )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set( [ filename_3_1, ] ) )
        self.assertEqual( dag.get( "filename_2_1" ).getParents(), set( [ filename_1_1 ] ) )

        self.assertEqual( dag.get( "filename_2_2" ).getChildren(), set( [ filename_3_1, ] ) )
        self.assertEqual( dag.get( "filename_2_2" ).getParents(), set( [ filename_1_1 ] ) )

        self.assertEqual( dag.get( "filename_3_1" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_3_1" ).getParents(), set( [ filename_2_1, filename_2_2 ] ) )

    def test_cycle( self ):
        dag = Dag()

        # filename_1_1
        #   filename_2_1
        #       filename_1_1

        filename_1_1 = DagNode( "filename_1_1" )
        filename_2_1 = DagNode( "filename_2_1" )

        dag.add( 1, "filename_1_1" )
        dag.add( 2, "filename_2_1" )
        dag.add( 3, "filename_1_1" )

        self.assertEqual( dag.get( "filename_1_1" ).getChildren(), set( [ filename_2_1 ] ) )
        self.assertEqual( dag.get( "filename_1_1" ).getParents(), set( [ dag.getRoot() ] ) )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_2_1" ).getParents(), set( [ filename_1_1 ] ) )

    def test_one_node_twice( self ):
        dag = Dag()

        # filename_1_1
        #   filename_2_1
        #      filename_1_1
        #         filename_3_1

        filename_1_1 = DagNode( "filename_1_1" )
        filename_2_1 = DagNode( "filename_2_1" )
        filename_3_1 = DagNode( "filename_3_1" )

        dag.add( 1, "filename_1_1" )
        dag.add( 2, "filename_2_1" )
        dag.add( 3, "filename_1_1" )
        dag.add( 4, "filename_3_1" )

        self.assertEqual( dag.get( "filename_1_1" ).getChildren(), set( [ filename_2_1, filename_3_1 ] ) )
        self.assertEqual( dag.get( "filename_1_1" ).getParents(), set( [ dag.getRoot() ] ) )

        self.assertEqual( dag.get( "filename_2_1" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_2_1" ).getParents(), set( [ filename_1_1 ] ) )

        self.assertEqual( dag.get( "filename_3_1" ).getChildren(), set() )
        self.assertEqual( dag.get( "filename_3_1" ).getParents(), set( [ filename_1_1 ] ) )
#
# main
#
if __name__ == "__main__":
    unittest.main()

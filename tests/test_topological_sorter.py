import unittest

from topological_sorter import\
    TopologicalSorter

from dag import\
    Dag,\
    DfsNode

#
# TestTopologicalSorter
#
class TestTopologicalSorter( unittest.TestCase ):
    def test_1( self ):
        dag = Dag()

        # . a
        # . b
        # . c

        self._a = dag.add( 1, "a" )
        self._b = dag.add( 1, "b" )
        self._c = dag.add( 1, "c" )

        tSorter = TopologicalSorter( dag )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( [ i.getData() for i in tSorter.getNodes() ], [ "b", "c", "a" ] )

    def test_2( self ):
        dag = Dag()

        # . a
        # .. c
        # .. b
        # ... c

        self._a = dag.add( 1, "a" )
        self._c = dag.add( 2, "c" )
        self._b = dag.add( 2, "b" )
        self._c = dag.add( 3, "c" )

        tSorter = TopologicalSorter( dag )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( [ i.getData() for i in tSorter.getNodes() ], [ "a", "b", "c" ] )
#
# main
#
if __name__ == "__main__":
    unittest.main()

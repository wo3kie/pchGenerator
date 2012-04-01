import unittest

from topological_sorter import\
    TopologicalSorter

from dag import\
    Dag

#
# TestSopologicalSorter
#
class TestSopologicalSorter( unittest.TestCase ):
    def test_1( self ):
        dag = Dag()

        # . a
        # . b
        # . c

        dag.add( 1, "a" )
        dag.add( 1, "b" )
        dag.add( 1, "c" )

        tSorter = TopologicalSorter( dag )

        self.assertEqual( [ i.getData() for i in tSorter.getNodes() ], [ "root", "b", "c", "a" ] )

    def test_2( self ):
        dag = Dag()

        # . a
        # .. c
        # .. b
        # ... c

        dag.add( 1, "a" )
        dag.add( 2, "c" )
        dag.add( 2, "b" )
        dag.add( 3, "c" )

        tSorter = TopologicalSorter( dag )

        self.assertEqual( [ i.getData() for i in tSorter.getNodes() ], [ "root", "a", "b", "c" ] )
#
# main
#
if __name__ == "__main__":
    unittest.main()

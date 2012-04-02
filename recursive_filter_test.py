import unittest

from headers_dag import\
    HeadersDag

from topological_sorter import\
    TopologicalSorter

from recursive_filter import\
    RecursiveFilter

#
# TestRecursiveFilter
#
class TestRecursiveFilter( unittest.TestCase ):
    def setUp( self ):
        self._dag = HeadersDag()

        self._a = self._dag.add( 1, "a" )
        self._b = self._dag.add( 2, "b" )
        self._c = self._dag.add( 3, "c" )
        self._c = self._dag.add( 2, "c" )

        self._tSorter = TopologicalSorter( self._dag )

    def test_1( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: x.getData() == "a") )

        self.assertEqual( rFilter.getNodes(), [ self._a ] )

    def test_2( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: x.getData() == "b") )

        self.assertEqual( rFilter.getNodes(), [ self._b ] )

    def test_3( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: x.getData() == "c") )

        self.assertEqual( rFilter.getNodes(), [ self._c ] )

    def test_4( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: True) )

        self.assertEqual( rFilter.getNodes(), [ self._dag.getRoot() ] )

    def test_5( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: False) )

        self.assertEqual( rFilter.getNodes(), [] )

#
# main
#
if __name__ == "__main__":
    unittest.main()

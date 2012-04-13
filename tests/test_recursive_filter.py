import unittest

from dag import DfsNode
from headers_dag import HeadersDag
from topological_sorter import TopologicalSorter
from recursive_filter import RecursiveFilter

#
# OptionsMock
#
class OptionsMock:
    def __init__( self ):
        self.watch_header = ""

#
# TestRecursiveFilter
#
class TestRecursiveFilter( unittest.TestCase ):
    def setUp( self ):
        self._dag = HeadersDag()

        # a
        #  b
        #   c
        #  c

        self._a = self._dag.add( 1, "a" )
        self._b = self._dag.add( 2, "b" )
        self._c = self._dag.add( 3, "c" )
        self._c = self._dag.add( 2, "c" )
        self._dag.processOneFile()

        self._options = OptionsMock()

        self._tSorter = TopologicalSorter( self._dag )

    def test_1( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: x.getData() == "a"), self._options )

        self.assertFalse( self._a.isIncluded() )
        self.assertFalse( self._b.isIncluded() )
        self.assertFalse( self._c.isIncluded() )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( rFilter.getNodes(), [ self._a ] )

    def test_2( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: x.getData() == "b"), self._options )

        self.assertFalse( self._a.isIncluded() )
        self.assertFalse( self._b.isIncluded() )
        self.assertFalse( self._c.isIncluded() )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( rFilter.getNodes(), [ self._b ] )

    def test_3( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: x.getData() == "c"), self._options )

        self.assertFalse( self._a.isIncluded() )
        self.assertFalse( self._b.isIncluded() )
        self.assertFalse( self._c.isIncluded() )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( rFilter.getNodes(), [ self._c ] )

    def test_4( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: True), self._options )

        self.assertFalse( self._a.isIncluded() )
        self.assertFalse( self._b.isIncluded() )
        self.assertFalse( self._c.isIncluded() )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( rFilter.getNodes(), [ self._a ] )

    def test_5( self ):
        rFilter = RecursiveFilter( self._tSorter, (lambda x: False), self._options )

        self.assertFalse( self._a.isIncluded() )
        self.assertFalse( self._b.isIncluded() )
        self.assertFalse( self._c.isIncluded() )

        self.assertEqual( self._a.getColor(), DfsNode.White )
        self.assertEqual( self._b.getColor(), DfsNode.White )
        self.assertEqual( self._c.getColor(), DfsNode.White )

        self.assertEqual( rFilter.getNodes(), [] )

#
# main
#
if __name__ == "__main__":
    unittest.main()

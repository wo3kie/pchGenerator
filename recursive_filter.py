from topological_sorter import\
    TopologicalSorter

#
# RecursiveFilter
#
class RecursiveFilter:
    def __init__( self, tSorter, predicate, options ):
        self._filteredNodes = []
        self._tSorter = tSorter
        self._options = options

        for node in self._tSorter.getNodes():
            self.__filter( node, predicate )

        self.__cleanUp()

    def __filter( self, node, predicate ):
        if predicate( node ) == False:
            return

        if node.isIncluded():
            if self._options.watch_header == node.getData():
                node.setFailingReason( "Header already included by other header" )

            return

        self._filteredNodes.append( node )

        node.setIncluded( True )

        for child in node.getChildren():
            child.setIncludedRecursively( True )

    def __cleanUp( self ):
        for node in self._filteredNodes:
            node.setIncludedRecursively( False )

    def getNodes( self ):
        return self._filteredNodes

    def getRoot( self ):
        return self._tSorter.getRoot()

from topological_sorter import\
    TopologicalSorter

#
# RecursiveFilter
#
class RecursiveFilter:
    def __init__( self, tSorter, predicate, options ):
        self._filteredNodes = []
        self._options = options

        for item in tSorter.getNodes():
            self.__markedAsIncludedRecursively( item, False )

        for item in tSorter.getNodes():
            self.__filter( item, predicate )

    def __len__( self ):
        return len( self._filteredNodes )

    def __filter( self, node, predicate ):
        if predicate( node ) == False:
            return

        if node.isIncluded():
            return

        self._filteredNodes.append( node )

        node.setIncluded( True )

        for child in node.getChildren():
            self.__markedAsIncludedRecursively( child, True )

    def __markedAsIncludedRecursively( self, node, value ):
        if node.isIncluded() == value:
            return

        node.setIncluded( value )

        if self._options.watch_header == node.getData():
            node.setFailingReason( "Header already included by other header" )

        for child in node.getChildren():
            self.__markedAsIncludedRecursively( child, True )

    def getNodes( self ):
        return self._filteredNodes


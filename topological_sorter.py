from dag import\
    DfsNode

import copy

#
# TopologicalSorter:
#
class TopologicalSorter:
    def __init__( self, dag ):
        self._counter = 0

        self.__calculatePrePostTime( dag.getRoot() )

        self._sortedNodes = [ dag.getRoot() ]
        for item in dag.getNodes():
            self._sortedNodes.append( item )

        self._sortedNodes.sort( reverse=True, key=(lambda x: x.getPostVisit() ) )

    def __calculatePrePostTime( self, node ):
        assert node.getColor() != DfsNode.Grey, "no cycles allowed"

        if node.getColor() == DfsNode.Black:
            return

        node.setColor( DfsNode.Grey )

        self._counter += 1
        node.setPreVisit( self._counter )

        for child in node.getChildren():
            self.__calculatePrePostTime( child )

        node.setColor( DfsNode.Black )

        self._counter += 1
        node.setPostVisit( self._counter )

    def getNodes( self ):
        return self._sortedNodes

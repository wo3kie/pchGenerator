from dag import\
    DfsNode

import copy

#
# TopologicalSorter:
#
class TopologicalSorter:
    def __init__( self, dag ):
        self._counter = 0
        self._dag = dag
        self._sortedNodes = []

        self.__sort()

        self.__cleanUp()

    def __sort( self ):
        self.__calculatePrePostTime( self.getRoot() )

        for item in self._dag.getNodes():
            self._sortedNodes.append( item )

        self._sortedNodes.sort( reverse=True, key=(lambda x: x.getPostVisit() ) )

    def __calculatePrePostTime( self, node ):
        assert node.getColor() != DfsNode.Grey, "no cycles allowed: {0}".format( node.getData() )

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

    def __cleanUp( self ):
        self.getRoot().setColor( DfsNode.Black )
        self.getRoot().setColorRecursively( DfsNode.White )

    def getNodes( self ):
        return self._sortedNodes

    def getRoot( self ):
        return self._dag.getRoot()


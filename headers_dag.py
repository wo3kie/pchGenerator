from dag import\
    DfsNode,\
    DagNode,\
    Dag

#
# Header Node
#
class HeaderNode( DagNode ):
    def __init__( self, value ):
        DagNode.__init__( self, value )

        self._included = False
        self._counter = 0

    def setIncluded( self, value ):
        self._included = value

    def isIncluded( self ):
        return self._included

    def setCounter( self, value ):
        self._counter = value

    def getCounter( self ):
        return self._counter

#
# Header DAG
#
class HeadersDag( Dag ):
    def __init__( self ):
        Dag.__init__( self, HeaderNode )

    def add( self, depth, header ):
        node = Dag.add( self, depth, header )
        self.__markRecursivelyAsIncluded( node )
        return node

    def processOneFile( self ):
        for child in self.getRoot().getChildren():
            self.__processOneFile( child )

    def __markRecursivelyAsIncluded( self, node ):
        if node.isIncluded() == True:
            return

        node.setIncluded( True )

        for child in node.getChildren():
            self.__markRecursivelyAsIncluded( child )

    def __processOneFile( self, node ):
        if node.isIncluded() == False:
            return

        node.setCounter( node.getCounter() + 1 )
        node.setIncluded( False )

        for child in node.getChildren():
            self.__processOneFile( child )

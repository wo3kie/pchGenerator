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
        self._reason = "File included in precompiled header"

    def setIncluded( self, value ):
        self._included = value

    def isIncluded( self ):
        return self._included

    def setIncludedRecursively( self, value ):
        if self.isIncluded() == value:
            return

        self.setIncluded( value )

        for child in self.getChildren():
            child.setIncludedRecursively( value )

    def setCounter( self, value ):
        self._counter = value

    def getCounter( self ):
        return self._counter

    def setFailingReason( self, reason ):
        self._reason = reason

    def getFailingReason( self ):
        return self._reason

#
# Header DAG
#
class HeadersDag( Dag ):
    def __init__( self ):
        Dag.__init__( self, HeaderNode )

    def add( self, depth, header ):
        node = Dag.add( self, depth, header )
        node.setIncludedRecursively( True )
        return node

    def update( self, depth, header ):
        return Dag.add( self, depth, header )

    def processOneFile( self ):
        for child in self.getRoot().getChildren():
            self.__processOneFile( child )

    def __processOneFile( self, node ):
        if node.isIncluded() == False:
            return

        node.setCounter( node.getCounter() + 1 )
        node.setIncluded( False )

        for child in node.getChildren():
            self.__processOneFile( child )

#
# DagNode
#
class DagNode:
    def __init__( self, data ):
        self._data = data

        self._parents = set()
        self._children = set()

    def __eq__( self, other ):
        return self.getData() == other.getData()

    def __hash__( self ):
        return self._data.__hash__()

    def deepPrint( self, indent = 0 ):
        print( indent * ' ', self._data )

        for child in self.getChildren():
            child.deepPrint( indent + 1 )

    def getData( self ):
        return self._data

    def setData( self, data ):
        self._data = data

    def addChild( self, node ):
        self._children.add( node )

    def getChildren( self ):
        return self._children

    def addParent( self, node ):
        self._parents.add( node )

    def getParents( self ):
        return self._parents

from stack import Stack

#
# Dag
#
class Dag:
    def __init__( self ):
        self._nodes = {}
        self._stack = Stack()

        self._stack.push( DagNode( "root" ) )

        self._root = self._stack.top()

    def __areConnected( self, node1, node2 ):
        return node2 in node1.getChildren()

    def __connect( self, node1, node2 ):
        node1.addChild( node2 )
        node2.addParent( node1 )

    def __getDepth( self ):
        return self._stack.size() - 1

    def __getOrCreate( self, object ):
        if object not in self._nodes:
            self._nodes[ object ] = DagNode( object )

        return self._nodes[ object ]

    def get( self, object ):
        if object not in self._nodes:
            raise Exception( "object does not exist" )

        return self._nodes[ object ]

    def deepPrint( self ):
        self._root.deepPrint()

    def getRoot( self ):
        return self._root

    def add( self, depth, object ):
        assert depth > 0, 'depth cant be less equal zero'

        if depth > self.__getDepth() + 1:
            raise Exception( "Wrong depth, stack: ", self.__getDepth(), ", depth: ", depth )

        depthDifference = self.__getDepth() - depth + 1

        for i in range( 0, depthDifference ):
            self._stack.pop()

        assert self._stack.empty() == False, 'stack cant be empty'

        header = self.__getOrCreate( object )

        if self.__areConnected( self._stack.top(), header ) == False:
            self.__connect( self._stack.top(), header )

        self._stack.push( header )

    def size( self ):
        return len( self._nodes )

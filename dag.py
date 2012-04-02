#
# DfsNode
#
class DfsNode:
    White = 0
    Grey = 1
    Black = 2

    def __init__( self ):
        self._preVisit = -1
        self._postVisit = -1

        self._color = DfsNode.White

    def setColor( self, color ):
        assert color in ( DfsNode.White, DfsNode.Grey, DfsNode.Black ), "invalid color value"

        self._color = color

    def getColor( self ):
        return self._color

    def setPreVisit( self, time ):
        self._preVisit = time

    def getPreVisit( self ):
        return self._preVisit

    def setPostVisit( self, time ):
        if time <= self.getPreVisit():
            raise Exception( "wrong post visit time: ", self.getPreVisit(), ", ", self.getPostVisit() )

        self._postVisit = time

    def getPostVisit( self ):
        return self._postVisit

#
# DagNode
#
class DagNode( DfsNode ):
    def __init__( self, data ):
        DfsNode.__init__( self )

        self._data = data

        self._parents = set()
        self._children = set()

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

    def isRoot( self ):
        return len( self.getParents() ) == 0

    def isLeaf( self ):
        return len( self.getChildren() ) == 0

    def setColorRecursively( self, color ):
        if self.getColor() == color:
            return

        self.setColor( color )

        for child in self.getChildren():
            child.setColorRecursively( color )

    def deepPrint( self, indent = 0 ):
        print( indent * ' ', self._data )

        for child in self.getChildren():
            child.deepPrint( indent + 1 )

    def __eq__( self, other ):
        return self.getData() == other.getData()

    def __hash__( self ):
        return self._data.__hash__()

from stack import Stack

#
# Dag
#
class Dag:
    def __init__( self, type = DagNode ):
        self._type = type

        self._nodes = {}
        self._stack = Stack()

        self._stack.push( self._type( "root" ) )

        self._root = self._stack.top()

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
            if self.__checkForCycle( self._stack.top(), header ):
                return header

            self.__connect( self._stack.top(), header )

        self._stack.push( header )

        return header

    def get( self, object ):
        if object not in self._nodes:
            raise Exception( "object does not exist" )

        return self._nodes[ object ]

    def getNodes( self ):
        return self._nodes.values()

    def getRoot( self ):
        return self._root

    def deepPrint( self ):
        self._root.deepPrint()

    def __areConnected( self, node1, node2 ):
        return node2 in node1.getChildren()

    def __connect( self, node1, node2 ):
        node1.addChild( node2 )
        node2.addParent( node1 )

    def __getDepth( self ):
        return self._stack.size() - 1

    def __getOrCreate( self, object ):
        if object not in self._nodes:
            self._nodes[ object ] = self._type( object )

        return self._nodes[ object ]

    def __checkForCycle( self, parent, node ):
        result = self.__checkForCycleImpl( parent, node )

        node.setColorRecursively( DfsNode.White )

        return result

    def __checkForCycleImpl( self, parent, node ):
        if node.getColor() == DfsNode.Black:
            return False

        node.setColor( DfsNode.Black )

        if parent == node:
            return True

        for child in node.getChildren():
            if self.__checkForCycleImpl( parent, child ) == True:
                return True

        return False

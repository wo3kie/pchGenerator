# pchGenerator

import sys

from stack import Stack

from headers_dag import HeaderNode, HeadersDag

from topological_sorter import TopologicalSorter

from recursive_filter import RecursiveFilter

#
# printHelp
#
def printHelp():
    print( "Usage: ", sys.argv[0] )
    print( "Author: Lukasz Czerwinski (wo3kie@gmail.com)" )

#
# parseLine
#
def parseLine( line ):
    i = 0
    length = len( line )

    while i < length and line[i] == '.':
        i += 1

    if i == 0:
        raise Exception( "Wrong line format: 'filename'" )

    if line[i] != ' ':
        raise Exception( "Wrong line format: '...filename'" )

    if i + 1 == length:
        raise Exception( "Wrong line format: '... '" )

    return ( i, line[ i + 1 : len(line) ] )

#
# isApplicationHeader
#
def isApplicationHeader( node ):
    return node.getData().startswith( "path/to/my/project" )

#
# isFirstLevelApplicationLevel
#
def isFirstLevelNonApplicationHeader( node ):
    if isApplicationHeader( node ) == True:
        return False

    for parent in node.getParents():
        if parent.isRoot():
            return True

        if isApplicationHeader:
            return True

    return False

#
# shouldBeInPCH
#
def shouldBeInPCH( node ):
    return isFirstLevelNonApplicationHeader( node )

#
# runApplication
#
def runApplication():
    if len( sys.argv ) != 2:
        printHelp()
        exit( 1 )

    file = open( sys.argv[1], 'r' )

    dag = HeadersDag()

    for line in file:
        depth, file = parseLine( line.strip() )
        dag.add( depth, file )

    dag.processOneFile()

    tSorter = TopologicalSorter( dag )

    rFilter = RecursiveFilter( tSorter, shouldBeInPCH )

    for i in rFilter.getNodes():
        print( i.getData() )
#
# main
#
if __name__ == "__main__":
    runApplication()

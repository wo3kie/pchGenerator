# pchGenerator

import sys

from stack import Stack

from dag import DagNode, Dag

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
# runApplication
#
def runApplication():
    if len( sys.argv ) != 2:
        printHelp()
        exit( 1 )

    file = open( sys.argv[1], 'r' )

    dag = Dag()

    for line in file:
        depth, file = parseLine( line )

        dag.add( depth, file )

#
# main
#
if __name__ == "__main__":
    runApplication()

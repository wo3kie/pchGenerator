from headers_dag import HeaderNode
from process_argv import processArgv
from should_be_in_pch import ShouldBeInPCH

import unittest

#
# TestShouldBeInPCH
#
class TestShouldBeInPCH( unittest.TestCase ):
    def test_threshold_1( self ):
        options = processArgv( [ "-t", "50", "-p", "/project", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node = HeaderNode( "/library/test.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )
        
        self.assertEqual( inPCH( node ), True )

    def test_threshold_2( self ):
        options = processArgv( [ "-t", "50", "-p", "/project", "test.cpp", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node = HeaderNode( "test.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )
        
        self.assertEqual( inPCH( node ), True )

    def test_threshold_3( self ):
        options = processArgv( [ "-t", "40", "-p", "/project", "test.cpp", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node = HeaderNode( "test.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )
        
        self.assertEqual( inPCH( node ), True )

    def test_threshold_4( self ):
        options = processArgv( [ "-t", "80", "-p", "/project", "test.cpp", "test.cpp", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node = HeaderNode( "test.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )
        
        self.assertEqual( inPCH( node ), False )

    def test_threshold_5( self ):
        options = processArgv( [ "-t", "80", "-p", "/project", "test.cpp", "test.cpp", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node = HeaderNode( "test.hpp" )
        node.addParent( parent )
        node.setCounter( 2 )
        
        self.assertEqual( inPCH( node ), True )

    def test_exclude( self ):
        options = processArgv( [ "-e", "boost", "-p", "/project", "--", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node1 = HeaderNode( "boost/..." )
        node1.addParent( parent )
        node1.setCounter( 1 )

        self.assertEqual( inPCH( node1 ), False )
        
        node2 = HeaderNode( ".../boost/..." )
        node2.addParent( parent )
        node2.setCounter( 1 )

        self.assertEqual( inPCH( node2 ), False )
        
        node3 = HeaderNode( "/stl/..." )
        node3.addParent( parent )
        
        self.assertEqual( inPCH( node3 ), True )

    def test_exclude_except( self ):
        options = processArgv( [ "-e", "boost", "-x", "thread", "shared_ptr", "-p", "/project", "--", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )
        
        node1 = HeaderNode( "boost/tokenizer" )
        node1.addParent( parent )
        node1.setCounter( 1 )

        self.assertEqual( inPCH( node1 ), False )
        
        node2 = HeaderNode( "/boost/thread" )
        node2.addParent( parent )
        node2.setCounter( 1 )

        self.assertEqual( inPCH( node2 ), True )
        
        node3 = HeaderNode( "/boost/shared_ptr" )
        node3.addParent( parent )
        
        self.assertEqual( inPCH( node3 ), True )
        
        node4 = HeaderNode( "/stl/..." )
        node4.addParent( parent )
        
        self.assertEqual( inPCH( node4 ), True )

    def test_application_header_1( self ):
        options = processArgv( [ "-p", "/project", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )

        node = HeaderNode( "/home/main.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )

        self.assertEqual( inPCH( node ), True )

    def test_application_header_2( self ):
        options = processArgv( [ "-p", "/project", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )

        node = HeaderNode( "/project/main.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )

        self.assertEqual( inPCH( node ), False )
        
    def test_application_header_3( self ):
        options = processArgv( [ "-p", "test", "test.cpp" ] )

        inPCH = ShouldBeInPCH( options )

        parent = HeaderNode( "root" )

        node = HeaderNode( "test.hpp" )
        node.addParent( parent )
        node.setCounter( 1 )

        deepNode = HeaderNode( "test.impl.hpp" )
        deepNode.addParent( node )
        deepNode.setCounter( 1 )

        self.assertEqual( inPCH( deepNode ), False )

#
# main
#
if __name__ == "__main__":
    unittest.main()

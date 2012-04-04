#
# GCCFacade
#
class GCCFacade:
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
        
    def name():
        return "g++"
        
    def removeCompilationOption( options ):
        return options.replace( "-c", "" )
        
    def runPreprocessingOnly( options ):
        return "-H " + options
        
    def processCompOptions( options ):
        options = GCCFacade.removeCompilationOption( options )
        options = GCCFacade.runPreprocessingOnly( options )
        
        return options.strip()

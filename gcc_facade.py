#
# GCCFacade
#
class GCCFacade:
    @staticmethod
    def parseLine( line ):
        i = 0
        length = len( line )

        while i < length and line[i] == '.':
            i += 1

        if i == 0:
            raise Exception( "Wrong line format: ", line )

        if line[i] != ' ':
            raise Exception( "Wrong line format: ", line )

        if i + 1 == length:
            raise Exception( "Wrong line format: ", line )

        return ( i, line[ i + 1 : len(line) ] )
        
    @staticmethod
    def name():
        return "g++"
    
    @staticmethod
    def removeCompilationOption( options ):
        return options.replace( "-c", "" )
        
    @staticmethod
    def runPreprocessingOnly( options ):
        return "-E -H " + options
        
    @staticmethod
    def processCompOptions( options ):
        options = GCCFacade.removeCompilationOption( options )
        options = GCCFacade.runPreprocessingOnly( options )
        
        return options.strip()

import subprocess

#
# GCCFacade
#
class GCCFacade:
    @staticmethod
    def processCompOptions( options ):
        options = GCCFacade.__removeCompilationOption( options )
        options = GCCFacade.__runPreprocessingOnly( options )

        return options.strip()

    @staticmethod
    def getHeaders( filename, options ):
        args = GCCFacade.__name()
        args += " " + options
        args += " " + filename

        proc = subprocess.Popen(
            args,
            shell = True,
            stdin = subprocess.PIPE,
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines=True
        )

        stdout_output, stderr_output = proc.communicate()

        return stderr_output

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
    def __name():
        return "g++"

    @staticmethod
    def __removeCompilationOption( options ):
        return options.replace( "-c", "" )

    @staticmethod
    def __runPreprocessingOnly( options ):
        return "-E -H " + options

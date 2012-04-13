from math import floor

#
# ShouldBeInPCH
#
class ShouldBeInPCH:
    def __init__( self, options ):
        self._options = options

        self._options.threshold = self.__calculateThreshold()

    def __call__( self, node ):
        isFileTypeOK = self.__isFirstLevelNonApplicationHeader( node )
        isThresholdOK = self.__checkThreshold( node )
        isExclusionOK = self.__checkExclusion( node )

        if self._options.watch_header == node.getData():
            if isFileTypeOK == False: node.setFailingReason( "Included by other non application header" )
            if isThresholdOK == False: node.setFailingReason( "Threshold is too high for this header" )
            if isExclusionOK == False: node.setFailingReason( "Header excluded by pattern" )

        return isFileTypeOK and isThresholdOK and isExclusionOK

    def __calculateThreshold( self ):
        threshold = self._options.threshold
        numberOfFiles = len( self._options.files )

        return floor( max( 1, numberOfFiles * threshold ) / 100 )

    def __isFirstLevelNonApplicationHeader( self, node ):
        if self.__isApplicationHeader( node ) == True:
            return False

        for parent in node.getParents():
            if parent.isRoot():
                return True

            if self.__isApplicationHeader( parent ):
                return True

        return False

    def __isApplicationHeader( self, node ):
        return node.getData().startswith( self._options.project_path )

    def __checkThreshold( self, node ):
        return node.getCounter() >= self._options.threshold

    def __checkExclusion( self, node ):
        if self.__findAnyOf( node.getData(), self._options.exclude_except ):
            return True

        if self.__findAnyOf( node.getData(), self._options.exclude ):
            return False

        return True

    def __findAnyOf( self, value, patterns ):
        for pattern in patterns:
            if value.find( pattern ) != -1:
                return True

        return False

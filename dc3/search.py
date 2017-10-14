class Search():
    # Searchs using a preprocessed index
    def __init__(self, index, text):
        self.index = index
        self.text = text

    def search(self, pattern):
        upperBound = self.getUpperBound(0, len(self.index) - 1, pattern)
        upperMatchLen = self.getMatchLength(upperBound, pattern)
        if (upperMatchLen != len(pattern)):
            return (0,0)
        lowerBound = self.getLowerBound(0, len(self.index) - 1, pattern)
        return (lowerBound, upperBound + 1)

    def getMatchLength(self, idxPos, pattern):
        textPos = self.index[idxPos]
        for i in range (0, len(pattern)):
            if (self.text[textPos + i] != pattern[i]):
                return i
        return len(pattern)

    def getUpperBound(self, lowIdx, hiIdx, pattern):
        if lowIdx >= hiIdx:
            return lowIdx
        midIdx = int((lowIdx + hiIdx) / 2)
        midMatchLen = self.getMatchLength(int(midIdx), pattern)

        textPos = self.index[midIdx]
        if midMatchLen == len(pattern) or self.text[textPos + midMatchLen] < pattern[midMatchLen]:
            upper =self.getUpperBound(midIdx + 1, hiIdx, pattern)
            upperMatchLen = self.getMatchLength(upper, pattern) 
            if upperMatchLen < midMatchLen:
                return midIdx
            return upper
        
        return self.getUpperBound(lowIdx, midIdx - 1, pattern)

    def getLowerBound(self, lowIdx, hiIdx, pattern):
        if lowIdx == hiIdx:
            return lowIdx
        midIdx = int((lowIdx + hiIdx) / 2)
        midMatchLen = self.getMatchLength(int(midIdx), pattern)

        if midMatchLen == len(pattern):
            return self.getLowerBound(lowIdx, midIdx - 1, pattern)

        textPos = self.index[midIdx]
        if self.text[textPos + midMatchLen] < pattern[midMatchLen]:
            return self.getLowerBound(midIdx + 1, hiIdx, pattern)

        return self.getLowerBound(lowIdx, midIdx - 1, pattern)
        if lowIdx >= hiIdx:
            return lowIdx
        midIdx = int((lowIdx + hiIdx) / 2)
        midMatchLen = self.getMatchLength(int(midIdx), pattern)

        textPos = self.index[midIdx]
        if midMatchLen == len(pattern) or self.text[textPos + midMatchLen] > pattern[midMatchLen]:
            lower = self.getLowerBound(lowIdx, midIdx - 1, pattern)
            lowerMatchLen = self.getMatchLength(lower, pattern) 
            if lowerMatchLen < midMatchLen:
                return midIdx
            return lower
        
        return self.getLowerBound(midIdx + 1, hiIdx, pattern)

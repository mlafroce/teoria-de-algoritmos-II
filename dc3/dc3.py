import itertools

class Dc3():
    """Dc3 algorithm implementation"""
    def __init__(self):
        pass

    def process(self, text):
        self.codex = self._buildCodex(text)
        transformedText = self._encode(text)
        self.indexes = self._radixSort(transformedText)

    def _encode(self, text):
        transformedText = []
        for c in text:
            transformedText.append(self.codex.getId(c))
        return transformedText

    def _radixSort(self, values):
        dc3Rec = Dc3Recursive(values, self.codex.getCodexSize())
        return dc3Rec.process()

    def _buildCodex(self, text):
        charSet = set(text)
        return Codex(charSet)


class Dc3Recursive():
    it = 0

    def __init__(self, values, codexSize):
        print("\nIteration: ", Dc3Recursive.it)
        print("Alphabet size: ", codexSize)
        print("Values size: ", len(values))
        self.values = values
        self.values.append(0)
        self.values.append(0)
        self.codexSize = codexSize
        Dc3Recursive.it += 1

    def _createIndexes(self, top):
        indexes = []
        # R1 y R2
        for i in range(1, top, 3):
            indexes.append(i)
        for i in range(2, top, 3):
            indexes.append(i)
        return indexes

    def process(self):
        b12Sorted = self.radixSortB12()
        b0Sorted = self.radixSortB0(b12Sorted)
        b012 = self.merge(b0Sorted, b12Sorted)
        return b012

    def radixSortB12(self):
        indexes = self._createIndexes(len(self.values) - 2)
        
        # radix por letra 2 y 1
        radix = self._createRadix()
        for tripletIdx in range(2, 0, -1):
            indexes = self._sortTriplet(indexes, tripletIdx, radix)


        # En esta etapa ordeno y filtro
        hasDuped = False
        # Radix por la primer letra de la tripla
        self._clearRadix(radix)
        radixTops = [-1] * len(radix)
        for idx in indexes:
            curChar = self.values[idx]
            lastIdx = radixTops[curChar]
            radixValue = 1
            lastTriple = self.values[lastIdx : lastIdx+3]
            curTriple = self.values[idx : idx+3]
            if curTriple == lastTriple:
                hasDuped = True
                radixValue = 0
            radix[curChar].append((idx, radixValue))
            radixTops[curChar] = idx

        # Armo ranks
        numIndexes = len(indexes)
        ranks = [None] * numIndexes
        counter = -1
        for sublist in radix:
            for r in sublist:
                rankIdx = self._b12ToIndex(r[0], numIndexes)
                counter += r[1]
                ranks[rankIdx] = counter

        '''
        print("[RadixSortB12] Values: {}".format(self.values))
        print("[RadixSortB12] Indexes: {}".format(indexes))
        print("[RadixSortB12] Ranks: {}".format(ranks))
        print("[RadixSortB12] Max value: {}".format(radixIdx))
        '''

        if (hasDuped):
            # radixIdx: max value
            # ranks: indices unicos y ordenados
            dc3Rec = Dc3Recursive(ranks, counter)
            ranks = dc3Rec.process()
            numRanks = len(ranks)
            for i, ri in enumerate(ranks):
                indexes[i] = self._indexToB12(ri, numRanks)
                
        else:
            numRanks = len(ranks)
            for i, ri in enumerate(ranks):
                indexes[ri] = self._indexToB12(i, numRanks)
                
        self.ranks = ranks

        return indexes

    def radixSortB0(self, b12Sorted):
        b1Top = int((len(b12Sorted) + 1) / 2)
        b0Hints = []
        b0 = []
        if len(self.values) % 3 == 0:
            b0Hints.append(len(self.values) - 3)
        for hint in self.ranks:
            if hint < b1Top:
                b0Hints.append(hint * 3)
                if hint == b1Top:
                    break
        radix = self._createRadix()
        for idx in b0Hints:
            radix[self.values[idx]].append(idx)
        
        return list(itertools.chain.from_iterable(radix))
        

    def merge(self, b0, b12):
        b0Index = 0
        b12Index = 0
        b012 = []
        b012ranks = [None]*len(self.values)
        for i, rank in enumerate(b12):
            b012ranks[rank] = i
        b012ranks[len(b012ranks) - 1] = 0
        b012ranks[len(b012ranks) - 2] = 0

        lenB0 = len(b0)
        lenB12 = len(b12)
        while b0Index < lenB0 and b12Index < lenB12:
            b0AuxIdx = b0[b0Index]
            b12AuxIdx = b12[b12Index]
            compType = b12AuxIdx % 3
            
            b0First = self._isB0first(b0AuxIdx, b12AuxIdx, b012ranks, type=compType)
            if (b0First):
                b012.append(b0AuxIdx)
                b0Index += 1
            else:
                b012.append(b12AuxIdx)
                b12Index += 1

        b012 = b012 + b0[b0Index: len(b0)] + b12[b12Index: len(b12)]

        return b012

    def _createRadix(self):
        radix = [None] * (self.codexSize + 1)
        for i in range(0, len(radix)):
            radix[i] = list()
        return radix

    def _clearRadix(self, radix):
        for r in radix:
            del r[:]

    def _sortTriplet(self, indexes, tripletIdx, radix):
        for idx in indexes:
            radix[self.values[idx+tripletIdx]].append(idx)
        result = list(itertools.chain.from_iterable(radix))
        self._clearRadix(radix)
        return result

    def _getIdxPosition(self, idx, lenIdx):
        offset = 0
        if idx % 3 == 2:
            offset = int(lenIdx / 2) + lenIdx % 2
        return offset + int(idx / 3)

    def _indexToB12(self, idx, top):
        b1Top = int((top + 1) / 2)
        if (idx < b1Top):
            return idx * 3 + 1
        else:
            return (idx - b1Top) * 3 + 2

    def _b12ToIndex(self, idx, top):
        b1Top = int((top + 1) / 2)
        aux = int(idx / 3)
        if (idx % 3 == 1):
            return aux
        return aux + b1Top

    def _isB0first(self, b0AuxIdx, b12AuxIdx, b012ranks, type):
        b0cmp = self.values[b0AuxIdx : b0AuxIdx + type]
        b12cmp = self.values[b12AuxIdx : b12AuxIdx + type]
        if (b0cmp == b12cmp):
            return b012ranks[b0AuxIdx + type] < b012ranks[b12AuxIdx + type]
        return b0cmp < b12cmp


class Codex():
    """Codex for encoding and decoding strings"""
    def __init__(self, charSet):
        self.charToId = {}
        self.idToChar = {}
        orderedAlpha = list(charSet)
        orderedAlpha.sort()
        i = 0
        for c in orderedAlpha:
            i+=1
            self.charToId[c] = i
            self.idToChar[i] = c
        self.codexSize = i

    def getId(self, char):
        return self.charToId[char]

    def getCodexSize(self):
        return self.codexSize

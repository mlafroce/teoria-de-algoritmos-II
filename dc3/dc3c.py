# -*- coding: utf-8 -*-

import itertools
import cRadix

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

    #@profile
    def radixSortB12(self):
        indexes = self._createIndexes(len(self.values) - 2)
        
        # radix por letra 2, 1 y 0
        cRadix.dc3RadixB12(indexes, self.values, self.codexSize)

        # Ahora solo filtro
        #hasDuped = self._sortAndFilter(indexes, radix)
        dupedList = self._filter(indexes)

        # Armo ranks
        numIndexes = len(indexes)
        ranks = [None] * numIndexes
        counter = -1
        for i in range (0, numIndexes):
            rankIdx = self._b12ToIndex(indexes[i], numIndexes)
            counter += dupedList[i]
            ranks[rankIdx] = counter

        hasDuped = counter != (numIndexes - 1)

        
        print("[RadixSortB12] Values: {}".format(self.values))
        print("[RadixSortB12] Indexes: {}".format(indexes))
        print("[RadixSortB12] Ranks: {}".format(ranks))
        #print("[RadixSortB12] Max value: {}".format(radixIdx))
        

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
        b1Top = (len(b12Sorted) + 1) // 2
        b0Hints = []
        if len(self.values) % 3 == 0:
            b0Hints.append(len(self.values) - 3)
        # Me ayudo con los índices de B1 ordenados
        # Los ranks me dicen como está ordenado el array [[3n+1]+[3n+2]]
        # Ej: [1,4,7,10,2,5,8,11]
        # Ranks: [0,1,6,4,2,5,3,7]
        # 0->1, 1->4, 6->8, 4->2, 2->7, 5->5, 3->10, 7->11
        # Los ranks menores a b1Top me dicen como está ordenado B1
        # Es decir, ya tengo ordenado la segunda y tercer columna de B0
        for hint in self.ranks:
            if hint < b1Top:
                b0Hints.append(hint * 3)
                if hint == b1Top:
                    break

        radix = self._createRadix()
        for idx in b0Hints:
            radix[self.values[idx]].append(idx)
        #cRadix.dc3RadixB0(b0Hints, self.values, self.codexSize)
        
        return b0Hints
        

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

    def _filter(self, indexes):
        dupedList = [None] * len(indexes)
        lastIdx = -1
        for i, idx in enumerate(indexes):
            lastTriplet = self.values[lastIdx : lastIdx+3]
            curTriplet = self.values[idx : idx+3]
            tripletValue = 1
            if curTriplet == lastTriplet:
                tripletValue = 0
            dupedList[i] = tripletValue
            lastIdx = idx
            
        return dupedList

    def _getIdxPosition(self, idx, lenIdx):
        offset = 0
        if idx % 3 == 2:
            offset = (lenIdx // 2) + lenIdx % 2
        return offset + idx // 3

    def _indexToB12(self, idx, top):
        b1Top = (top + 1) // 2
        if (idx < b1Top):
            return idx * 3 + 1
        else:
            return (idx - b1Top) * 3 + 2

    def _b12ToIndex(self, idx, top):
        b1Top = (top + 1) // 2
        aux = idx // 3
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

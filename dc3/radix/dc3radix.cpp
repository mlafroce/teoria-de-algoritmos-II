/**
 * _sortTriplet(self, indexes, tripletIdx, radix):
 *
 * for idx in indexes:
 *     radix[self.values[idx+tripletIdx]].append(idx)
 *     result = list(itertools.chain.from_iterable(radix))
 *     self._clearRadix(radix)
 *     return result
 **/
#include <vector>
#include <iostream>
#include "dc3radix.h"
extern "C" {

void radixSort12(int* indexes, int indexSize,
    int* values, int valuesSize,
    int radixSize) {
    radixSort(indexes, indexSize, values, valuesSize, 2, radixSize);
    radixSort(indexes, indexSize, values, valuesSize, 1, radixSize);
}

void radixSort(int* indexes, int indexSize,
    int* values, int valuesSize,
    int tripletIdx, int radixSize) {
    std::vector<std::vector<int> > radix(radixSize+1);
    for (int i = 0; i < indexSize; ++i) {
        int curIdx = indexes[i];
        int radixIdx = values[curIdx + tripletIdx];
        radix[radixIdx].push_back(curIdx);
    }
    // Ahora plancho el radix
    int offset = 0;
    for (int ri = 0; ri < radixSize + 1; ++ri) {
        std::copy(radix[ri].begin(), radix[ri].end(), indexes + offset);
        offset += radix[ri].size();
    }
}

}
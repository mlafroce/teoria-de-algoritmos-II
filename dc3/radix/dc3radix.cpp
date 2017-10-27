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

void radixSort(int* indexes, int indexSize,
    int* values, int valuesSize,
    int radixSize) {
    Radix radix(indexes, indexSize, values, valuesSize, radixSize);
    radix.sort(2);
    radix.sort(1);
    radix.sort(0);
}

} // extern

Radix::Radix(int* indexes, int indexSize,
            int* values, int valuesSize, int radixSize) :
    indexSize(indexSize), indexes(indexes),
    valuesSize(valuesSize), values(values),
    radixSize(radixSize), radix(radixSize + 1) {}

void Radix::sort(int tripletIdx) {
    for (int i = 0; i < this->indexSize; ++i) {
        int curIdx = this->indexes[i];
        int radixIdx = this->values[curIdx + tripletIdx];
        this->radix[radixIdx].push_back(curIdx);
    }
    // Ahora plancho el radix
    int offset = 0;
    for (int ri = 0; ri < this->radixSize + 1; ++ri) {
        std::copy(radix[ri].begin(), radix[ri].end(), this->indexes + offset);
        offset += radix[ri].size();
        radix[ri].clear();
    }
}

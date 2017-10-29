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
#include <cmath>
#include "dc3radix.h"
#include <cstdio>

extern "C" {

void radixSort(MyVector indexes,
    MyVector values,
    int radixSize) {
    Radix radix(indexes.data, indexes.size,
        values.data, values.size, radixSize);
    radix.sort(2);
    radix.sort(1);
    radix.sort(0);
}

void radixSortB0(MyVector indexes,
    MyVector values,
    int radixSize) {
    Radix radix(indexes.data, indexes.size,
        values.data, values.size, radixSize);
    radix.sort(0);
}

} // extern

Radix::Radix(int* indexes, int indexSize,
            int* values, int valuesSize, int radixSize) :
    indexSize(indexSize), indexes(indexes),
    valuesSize(valuesSize), values(values),
    radixSize(radixSize) {}

void Radix::sort(int tripletIdx) {
    std::vector<std::vector<int> > radix(10);
    int maxDigits = log10(this->radixSize) + 1;
    for (int valueExp = 0; valueExp < maxDigits; ++valueExp) {
        int valueMod = pow(10, valueExp);
        for (int i = 0; i < this->indexSize; ++i) {
            int curIdx = this->indexes[i];
            int radixIdx = this->values[curIdx + tripletIdx];
            radixIdx = (radixIdx / valueMod) % 10;
            radix[radixIdx].push_back(curIdx);
        }
        // Ahora plancho el radix
        int offset = 0;
        for (int ri = 0; ri < 10; ++ri) {
            std::copy(radix[ri].begin(), radix[ri].end(),
                this->indexes + offset);
            offset += radix[ri].size();
            radix[ri].clear();
        }
    }
}

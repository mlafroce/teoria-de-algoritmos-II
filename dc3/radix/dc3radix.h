#ifndef __DC3RADIX_H__
#define __DC3RADIX_H__
#include <vector>

class Radix {
public:
    Radix(int* indexes, int indexSize,
          int* values, int valuesSize, int radixSize);
    void sort(int valueOffset);
private:
    int indexSize;
    int* indexes;
    int valuesSize;
    int* values;
    int radixSize;
    std::vector<std::vector<int> > radix;
};

extern "C" {

void radixSort(int* indexes, int indexSize,
    int* values, int valuesSize,
    int radixSize);
}

#endif // __DC3RADIX_H__

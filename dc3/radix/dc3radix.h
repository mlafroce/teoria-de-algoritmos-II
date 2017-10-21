#ifndef __DC3RADIX_H__
#define __DC3RADIX_H__

extern "C" {
void radixSort(int* indexes, int indexSize,
    int* values, int valuesSize,
    int tripletIdx, int radixSize);

void radixSort12(int* indexes, int indexSize,
    int* values, int valuesSize,
    int radixSize);
}

#endif // __DC3RADIX_H__

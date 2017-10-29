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
};

// Parte visible de la biblioteca

extern "C" {

struct MyVector {
    int* data;
    int size;
};

void radixSort(MyVector indexes,
    MyVector values,
    int radixSize);

void radixSortB0(MyVector indexes,
    MyVector values,
    int radixSize);
}


#endif // __DC3RADIX_H__

import ctypes

_radixDLL = ctypes.CDLL('radix/libradix.so')
'''
void radixSort(int* indexes, int indexSize,
    int* values, int valuesSize,
    int radixSize)
'''
_radixDLL.radixSort.argtypes = (ctypes.POINTER(ctypes.c_int), ctypes.c_int,
   ctypes.POINTER(ctypes.c_int), ctypes.c_int,
   ctypes.c_int)

def dc3Radix12(indexes, values, radixSize):
    global _radixDLL
    # Declaro el tipo array de enteros
    indexesArray = ctypes.c_int * len(indexes)
    valuesArray = ctypes.c_int * len(values)
    cIndexes = indexesArray(*indexes)
    cValues = valuesArray(*values)
    # Version CType del size del array
    cIndexesSize = ctypes.c_int(len(indexes))
    cValuesSize = ctypes.c_int(len(values))
    cRadixSize = ctypes.c_int(radixSize)
    result = _radixDLL.radixSort(cIndexes,
        cIndexesSize, cValues, cValuesSize,
        cRadixSize)
    _convertCtoPython(indexes, cIndexes)

def _convertCtoPython(indexes, cIndexes):
    for i in range(0, len(indexes)):
        indexes[i] = cIndexes[i]

import ctypes

class CVector(ctypes.Structure):
    _fields_ = [("data", ctypes.POINTER(ctypes.c_int)),
                ("size", ctypes.c_int)]

_radixDLL = ctypes.CDLL('radix/libradix.so')

'''
Ordena triplas con radixSort
void radixSort(MyVector indexes, MyVector values, int radixSize)
'''
_radixDLL.radixSort.argtypes = (CVector, CVector, ctypes.c_int)

'''
Ordena triplas con radixSort del primer caracter
void radixSortB0(MyVector indexes, MyVector values, int radixSize)
'''
_radixDLL.radixSortB0.argtypes = (CVector, CVector, ctypes.c_int)


def dc3RadixB12(indexes, values, radixSize):
    # Declaro el tipo array de enteros
    indexesArray = ctypes.c_int * len(indexes)
    valuesArray = ctypes.c_int * len(values)
    cIndexes = indexesArray(*indexes)
    cValues = valuesArray(*values)

    # Version CType del size del array
    cIndexesSize = ctypes.c_int(len(indexes))
    cValuesSize = ctypes.c_int(len(values))

    cIndexesVector = CVector(indexesArray(*indexes), cIndexesSize)
    cValuesVector = CVector(valuesArray(*values), cValuesSize)
    cRadixSize = ctypes.c_int(radixSize)
    result = _radixDLL.radixSort(
        cIndexesVector, cValuesVector, cRadixSize)
    _convertCtoPython(indexes, cIndexesVector.data)

#@profile
def dc3RadixB0(indexes, values, radixSize):
    # Declaro el tipo array de enteros
    indexesArray = ctypes.c_int * len(indexes)
    valuesArray = ctypes.c_int * len(values)
    cIndexes = indexesArray(*indexes)
    cValues = valuesArray(*values)

    # Version CType del size del array
    cIndexesSize = ctypes.c_int(len(indexes))
    cValuesSize = ctypes.c_int(len(values))

    cIndexesVector = CVector(cIndexes, cIndexesSize)
    cValuesVector = CVector(cValues, cValuesSize)
    cRadixSize = ctypes.c_int(radixSize)
    result = _radixDLL.radixSortB0(
        cIndexesVector, cValuesVector, cRadixSize)
    _convertCtoPython(indexes, cIndexesVector.data)

def _convertCtoPython(indexes, cIndexes):
    for i in range(0, len(indexes)):
        indexes[i] = cIndexes[i]

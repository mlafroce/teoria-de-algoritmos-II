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

def listToCVector(pyList):
    # Declaro el tipo array de enteros
    typeArray = ctypes.c_int * len(pyList)
    cArray = typeArray(*pyList)
    # Version CType del size del array
    cSize = ctypes.c_int(len(pyList))
    return CVector(cArray, cSize)

def dc3RadixB12(indexes, values, radixSize):
    
    cIndexesVector = listToCVector(indexes)
    cValuesVector = listToCVector(values)
    cRadixSize = ctypes.c_int(radixSize)
    #_radixDLL.ProfilerStart('out.prof')
    result = _radixDLL.radixSort(
        cIndexesVector, cValuesVector, cRadixSize)
    #_radixDLL.ProfilerStop('out.prof')
    _convertCtoPython(indexes, cIndexesVector.data)


def dc3RadixB0(indexes, values, radixSize):
    cIndexesVector = listToCVector(indexes)
    cValuesVector = listToCVector(values)
    cRadixSize = ctypes.c_int(radixSize)
    result = _radixDLL.radixSortB0(
        cIndexesVector, cValuesVector, cRadixSize)
    _convertCtoPython(indexes, cIndexesVector.data)

def _convertCtoPython(indexes, cIndexes):
    for i in range(0, len(indexes)):
        indexes[i] = cIndexes[i]

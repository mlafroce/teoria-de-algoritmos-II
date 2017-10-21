#include "dc3radix.h"
#include <iostream>

int main(int argc, char** argv) {
	int indexes[35] = {1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 41, 44, 47, 50};
	int values[56] = {3, 12, 9, 4, 1, 7, 12, 9, 4, 1, 13, 17, 5, 1, 16, 4, 9, 1, 5, 15, 16, 5, 1, 16, 5, 18, 16, 12, 1, 8, 11, 16, 5, 11, 16, 4, 1, 15, 5, 14, 1, 10, 17, 19, 1, 9, 4, 14, 6, 12, 2, 2, 2};
	radixSort(indexes, 35, values, 56, 2, 19);
	std::cout << "Imprimendo indexes casi ordenados: " ;
	for (int i = 0; i < 35; ++i) {
		std::cout << indexes[i] << " ";
	}
	radixSort(indexes, 35, values, 56, 1, 19);
	std::cout << "Imprimendo indexes ordenados: " ;
	for (int i = 0; i < 35; ++i) {
		std::cout << indexes[i] << " ";
	}
}
all: test libradix.so

test: dc3radix.cpp test.cpp
	$(CXX) -Wall -pedantic -o $@ dc3radix.cpp test.cpp

libradix.so: dc3radix.cpp
	$(CXX) -fPIC -shared -O3 -o $@ $?



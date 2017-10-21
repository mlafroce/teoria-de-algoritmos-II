if [ -z "$1" ]; then
  echo "Ingrese un testCase"
else
  python -m cProfile -s time mainC.py testData/$1 > profile/$1-c
  python -m cProfile -s time mainPy.py testData/$1 > profile/$1-py
fi

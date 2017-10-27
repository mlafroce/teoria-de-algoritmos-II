declare -a tests=("yabba" "randomNums100000" "randomNums200000" "randomNums400000" "randomNums800000" "randomNums1600000" "randomNums3200000")


for text in ${tests[@]}
do
    valgrind --tool=massif --log-file=massif/$text-c python mainC.py testData/$text
    valgrind --tool=massif --log-file=massif/$text-py python mainPy.py testData/$text
done

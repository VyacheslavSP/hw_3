import random
# просто для сокращения кода. понятно что можно прописать бинарный поиск руками
from bisect import bisect_left


def find_result(number_array, X):
    pos = bisect_left(number_array, X)
    if pos == 0:
        return number_array[0]
    if pos == len(number_array):
        return number_array[-1]
    before = number_array[pos - 1]
    after = number_array[pos]
    if after - X < X - before:
        return after
    else:
        return before


while (True):
    try:
        N = int(input("Введите количество элементов в массиве: "))
        X = float(input("ведите число, которое хотите проверить: "))
        if (N <= 0):
            raise
        else:
            break
    except:
        print("неккоректный ввод числа")
number_array = []
for i in range(N):
    number_array.append(random.randint(1, N))
print(number_array)
number_array.sort()
if (X <= 1):
    print("ближайшее число "+str(number_array[0]))
elif (X >= N):
    print("ближайшее число "+str(number_array[-1]))
else:
    print(find_result(number_array, X))

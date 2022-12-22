import random
# просто для сокращения кода. понятно что можно прописать бинарный поиск руками
from bisect import bisect_left


def find_result(number_array, x):
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
if (len(number_array) % 2 == 0):
    Up = int(N/2)
else:
    Up = int(N/2)+1
for i in range(N):
    number_array.append(random.randint(1, Up))
print(number_array)
if (X <= 1):
    # теория вероятности была давно забыта,поэтому не смог доказать математически. если при создании
    # массива старт и конец randint всегда присутвуют в массиве то можно давать ответ и не создавая этот массив
    print("ближайшее число "+str(number_array[0]))
elif (X >= N/2):
    print("ближайшее число "+str(number_array[-1]))
else:
    print(find_result(number_array, X))

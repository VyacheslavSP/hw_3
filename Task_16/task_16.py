import random

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
if (1 <= X <= N/2):
    number_array = []
    if (len(number_array) % 2 == 0):
        Up = int(N/2)
    else:
        Up = int(N/2)+1
    for i in range(N):
        # непонятно N/2 включительно или нет? в итоге сделал проверку на четность и массив делвется включительно
        number_array.append(random.randint(1, Up))
    print(number_array)
    count = number_array.count(X)
    if (count != 0):
        print("Число встречается " + str(count)+" раз")
    else:
        print("Число не встречается")
else:
    print("Число не встречается в ряде. массив не создавался")

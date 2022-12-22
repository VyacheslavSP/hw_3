from string import ascii_letters
eng_arr = [['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'], ['D', 'G'], ['B', 'C', 'M', 'P'], [
    'F', 'H', 'V', 'W', 'Y'], ['K'], ['Not'], ['Not'], ['J', 'X'], ['not'], ['Q', 'Z']]
rus_arr = [['А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'], ['Д', 'К', 'Л', 'М', 'П', 'У'], ['Б', 'Г', 'Ё', 'Ь', 'Я'], [
    'Й', 'Ы'], ['Ж', 'З', 'Х', 'Ц', 'Ч'], ['Not'], ['Not'], ['Ш', 'Э', 'Ю'], ['Not'], ['Ф', 'Щ', 'Ъ']]
str_input = input("Введите слово ")
i = 0
result = 0
str_input = str_input.upper()
if (len(str_input) != 0):
    while (i < len(str_input)):
        if (str_input[i].isalpha):  # если буква
            need_find = True
            if (str_input[i] in ascii_letters):  # английская буква
                Search_arr = eng_arr
            else:
                Search_arr = rus_arr
        else:
            need_find = False
            i = i+1
        if (need_find):
            for j in range(0, len(Search_arr)):
                for k in range(0, len(Search_arr[j])):
                    if (str_input[i] == Search_arr[j][k]):
                        result = result+(j+1)
        i = i+1
print(result)
# программа ест все, буквы,цифры, знаки препинания и работает с этим.
# если хотим как в задании получить слово- предварительно проверям на ввод через регулярное выражение на то что сивол не число, так же можно организовать проверку что все буквы одной раскладки
# сейчас логика построена так что есть вариант английские буквы и просто буквы,которые есть в isalpha т.е. мама на русском даст 6 очков а мама на монголькой раскладке 0 очков
# вариант с использованием пустых строк массива был оставлен как более универсальный, можно, например, представлять в виде ['D', 'G',2]и обращаться к последнему значению в найденой строке
# вероятно более строго следовало бы организовать проверку не через isalpha а напрямую раскручивать массив и сравнивать, хотябы через any
# но это увеличило бы код.A вот как программе определить что это именно слово а не набор букв не знаю. едиственное что приходит на ум
# это загрузить базу Большого Оксфордского словаря и Толкового словаря Ожегова, при этом придумывая что то с разделителями (из серии Йошкар-Ола это 1 слово), но это
# кажется выходящим за рамки задания да и потребует куда большего времени на написание

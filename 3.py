'''как это работает (пример)
[10,9, 2, 5, 3, 7,101,18] <- числа
 0  0  0  0  0  0  0  0   <- длины
 1  0  0  0  0  0  0  0  - тк 10 на первой позиции
 1  1  0  0  0  0  0  0  - 9<10, значит макс длина послед-ти, заканч-ся числом 9, равна 1 
 1  1  1  0  0  0  0  0  - 2<10 и 2<9,  значит макс длина послед-ти, заканч-ся числом 2, равна 1 
 1  1  1  2  0  0  0  0  - 2<10 и 2<9,  значит макс длина послед-ти, заканч-ся числом 2, равна 1
 1  1  1  2  2  0  0  0  - 3>2, у 2 значение макс длины равно 1, значит макс длина послед-ти,заканч-ся числом 3,равно 2
 1  1  1  2  2  3  0  0  - 7>3, у 3 значение макс длины равно 2, значит макс длина послед-ти,заканч-ся числом 7,равно 3
 1  1  1  2  2  3  4  0  - 101>7 и 101>3, у 7 значение макс длины равно 3, значит макс длина послед-ти,заканч-ся числом 101,равно 4
 1  1  1  2  2  3  4  4  - 18>7, у 7 значение макс длины равно 3, значит макс длина послед-ти,заканч-ся числом 18,равно 4
 '''

import sys

def func(values, saved):
    for i in range(len(values)): #проходим все числа массива
        max_ch = 0 #максимальная длина послед-ти, закан-ся текущим числом
        for j in range(i): #проходим элменты массмва до текущего
            if values[i] > values[j]: 
                max_ch = max(max_ch, saved[j]) 
        saved[i] = max_ch + 1 #сохраняем в saved макс длину послед-ти, заканч-ся текущим числом
    return saved

def get_answer(values, saved):
    res = [] #результат
    current = max(saved) #наибольшая длина
    ch = sys.maxsize #просто очень большое число
    for i in range(len(values) - 1, -1, -1): #идем с конца массива чисел
        if saved[i] == current and values[i] < ch:
            #если число имело в saved длину current и оно меньше чем предыдущее сохраненное
            res.append(values[i])
            current -= 1 #будем искать число, у которого макс длина меньше на 1
            ch = values[i]
    return res[::-1] #разворачиваем резлультат


values = [10, 9, 2, 5, 3, 7, 101, 18]
saved = [0] * len(values)
#каждому числу будет соответствовать длина наибольшей возрастающей посл-ти, заканч-ся этим числом
print(func(values, saved))
print(get_answer(values, saved))

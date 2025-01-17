"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit


# традиционный итератор с функцией append
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# списковое включение
def func_2(nums):
    return [i for i, j in enumerate(nums) if j % 2 == 0]


list_num_1 = [el for el in range(1000)]
list_num_2 = [el for el in range(10000)]
list_num_3 = [el for el in range(100000)]
print(timeit("func_1(list_num_1)", globals=globals(), number=1000))
print(timeit("func_2(list_num_1)", globals=globals(), number=1000))
print(timeit("func_1(list_num_2)", globals=globals(), number=1000))
print(timeit("func_2(list_num_2)", globals=globals(), number=1000))
print(timeit("func_1(list_num_3)", globals=globals(), number=1000))
print(timeit("func_2(list_num_3)", globals=globals(), number=1000))
"""
0.08650808300000001
0.08109195799999999
0.849792541
0.7822250829999999
8.259916916
7.8763520840000005
Из показателей видно что list comprehensions работает чуть быстрее обычного цикла и с 
увеличением операций скорость также растет в арифметической прогрессии.
"""
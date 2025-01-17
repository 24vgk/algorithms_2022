"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации
   заполнение словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации
   получение элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации
   удаление элемента словаря, оцените сложность в O-нотации
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""
from time import time

"""
Задание (a)
"""
n = 10 ** 5


def time_decorator(func):
    def timer(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'Время выполнения {func.__name__} - {end - start}')
        return result
    return timer


@time_decorator
def completion_list(list_x, num):  # O(n)
    """ Заполнение списка """
    for i in range(num):
        list_x.insert(0, i)


result_list = []
completion_list(result_list, n)


@time_decorator
def completion_dict(dict_x, num):  # О(1)
    """ Заполнение словаря"""
    for i in range(num):
        dict_x[i] = i


result_dict = {}
completion_dict(result_dict, n)


""" 
В данном примере операция заполнения словаря занимает меньше времени, 
но при этом если n = 10**3 то список заполнится на порядок быстрее.
Время выполнения completion_list - 1.660729169845581
Время выполнения completion_dict - 0.007547855377197266
"""

"""
Задание (b)
"""
x = 8888


@time_decorator
def receive_list(list_x, x):  # O(n)
    for i in list_x:
        if i == x:
            return x


@time_decorator
def receive_dict(dict_x, x):  # O(1)
    for i in dict_x:
        if i == x:
            return dict_x[i]


receive_list(result_list, x)
receive_dict(result_dict, x)

"""
В данном случае извлечение из списка должно происходить дольше так как система перебирает весь список пока не найдет 
искомое,а словарь это хэш-поиск.
Время выполнения receive_list - 0.002130746841430664
Время выполнения receive_dict - 0.00021409988403320312
"""
"""
Задание (с)
"""
x = 8888


@time_decorator
def removal_list(list_x, x):  # O(n)
    for i in list_x:
        if i == x:
            list_x.remove(x)


@time_decorator
def removal_dict(dict_x, x):  # O(1)
    for i in dict_x:
        if i == x:
            del dict_x[i]
            break


removal_list(result_list, x)
removal_dict(result_dict, x)

"""
Так же как и в предыдущем случае словарь отрабатывает задачу быстрее
Время выполнения removal_list - 0.003201007843017578
Время выполнения removal_dict - 0.0002090930938720703
"""
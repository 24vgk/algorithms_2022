"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно
что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

1) сравнить операции
append, pop, extend списка и дека и сделать выводы что и где быстрее

2) сравнить операции
appendleft, popleft, extendleft дека и соответствующих им операций списка
и сделать выводы что и где быстрее

3) сравнить операции получения элемента списка и дека
и сделать выводы что и где быстрее

Подсказка:
для того, чтобы снизить погрешность, желательно операции по каждой ф-ции
(append, pop и т.д.) проводить в циклах. Для замеров используйте timeit.
"""

from collections import deque
from timeit import timeit

# 1 ############################


def append(collections_x):
    for i in range(n):
        collections_x.append(i)
    return collections_x


def pop(collections_x):
    for i in range(n):
        collections_x.pop()
    return collections_x


def extend(collections_x):
    for i in range(n):
        collections_x.extend([1, 2, 3])
    return collections_x


# 2 ##############################


def appendleft_list(collections_x):
    for i in range(n):
        collections_x.insert(0, i)
    return collections_x


def appendleft_deque(collections_x):
    for i in range(n):
        collections_x.appendleft(i)
    return collections_x


def popleft_list(collections_x):
    for i in range(n):
        collections_x.pop(i)
    return collections_x


def popleft_deque(collections_x):
    for i in range(n):
        collections_x.popleft()
    return collections_x


def extendleft_list(collections_x):
    for i in range(n):
        collections_x.insert(0, [1, 2, 3])
    return collections_x


def extendleft_deque(collections_x):
    for i in range(n):
        collections_x.extendleft([1, 2, 3])
    return collections_x


# 3 ##############################


def get_elem_list(collections_x):
    for i in range(n):
        collections_x[i] = i
    return collections_x


def get_elem_deque(collections_x):
    for i in range(n):
        collections_x[i] = i
    return collections_x


if __name__ == '__main__':
    list_x = [i for i in range(10 ** 4)]
    deque_x = deque([i for i in range(10 ** 4)])
    n = 10 ** 3

print(f"append списка- {timeit('append(list_x.copy())', globals=globals(), number=100)}")
print(f"append очереди-{timeit('append(deque_x.copy())', globals=globals(), number=100)}")
print(f"pop списка - {timeit('pop(list_x.copy())', globals=globals(), number=100)}")
print(f"pop очереди - {timeit('pop(deque_x.copy())', globals=globals(), number=100)}")
print(f"extend списка - {timeit('extend(list_x.copy())', globals=globals(), number=100)}")
print(f"extend очереди - {timeit('extend(deque_x.copy())', globals=globals(), number=100)}")
print('*' * 10)
print(f"appendleft списка - {timeit('appendleft_list(list_x.copy())', globals=globals(), number=100)}")
print(f"appendleft очереди - {timeit('appendleft_deque(deque_x.copy())', globals=globals(), number=100)}")
print(f"popleft списка - {timeit('popleft_list(list_x.copy())', globals=globals(), number=100)}")
print(f"popleft очереди - {timeit('popleft_deque(deque_x.copy())', globals=globals(), number=100)}")
print(f"extendleft списка - {timeit('extendleft_list(list_x.copy())', globals=globals(), number=100)}")
print(f"extendleft очереди - {timeit('extendleft_deque(deque_x.copy())', globals=globals(), number=100)}")
print('*' * 10)
print(f"get_elem списка - {timeit('get_elem_list(list_x.copy())', globals=globals(), number=100)}")
print(f"get_elem очереди - {timeit('get_elem_deque(deque_x.copy())', globals=globals(), number=100)}")
"""
append списка- 0.007197958000000004
append очереди-0.011061249999999995
pop списка - 0.007903415999999996
pop очереди - 0.010617750000000009
extend списка - 0.012389042000000003
extend очереди - 0.019706041000000007
**********
appendleft списка - 0.36311658299999994
appendleft очереди - 0.012105874999999933
popleft списка - 0.163304334
popleft очереди - 0.010884749999999999
extendleft списка - 0.39323062499999994
extendleft очереди - 0.021904499999999993
**********
get_elem списка - 0.006291875000000058
get_elem очереди - 0.011173250000000134
"""
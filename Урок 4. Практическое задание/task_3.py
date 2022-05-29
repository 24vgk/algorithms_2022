"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через timeit

Обязательно предложите еще свой вариант решения!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!
"""
from timeit import timeit
from cProfile import run


def revers_1(num, revers_num=0):
    if num == 0:
        return
    else:
        num = num % 10
        revers_num = (revers_num + num / 10) * 10
        num //= 10
        revers_1(num, revers_num)


def revers_2(num, revers_num=0):
    while num != 0:
        num = num % 10
        revers_num = (revers_num + num / 10) * 10
        num //= 10
    return revers_num


def revers_3(num):
    num = str(num)
    revers_num = num[::-1]
    return revers_num


def revers_4(num):
    return ''.join(reversed(str(num)))


num = 1234567890

print('Рекурсия: ', timeit(f'revers_1({num})', globals=globals()))
print('Цикл: ', timeit(f'revers_2({num})', globals=globals()))
print('Срез: ', timeit(f'revers_3({num})', globals=globals()))
print('Реверс: ', timeit(f'revers_4({num})', globals=globals()))

run("revers_1(num)")
run("revers_2(num)")
run("revers_3(num)")
run("revers_4(num)")

"""
По результатам видно что срез самый быстрый по выполнению
задачи. 

Рекурсия:  0.33839162500000003
Цикл:  0.249689375
Срез:  0.23078637500000003
Реверс:  0.6103881250000001
"""


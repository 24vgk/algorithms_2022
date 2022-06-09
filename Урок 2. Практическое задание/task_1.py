"""
Задание 1.	Написать программу, которая будет складывать, вычитать,
умножать или делить два числа. Числа и знак операции вводятся пользователем.
После выполнения вычисления программа не должна завершаться, а должна
запрашивать новые данные для вычислений. Завершение программы должно
выполняться при вводе символа '0' в качестве знака операции. Если пользователь
вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна
сообщать ему об ошибке и снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.

Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ

Решите через рекурсию. В задании нельзя применять циклы.

Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
"""


class Error(Exception):
    """Базовый класс для других исключений"""
    pass


class ValueSingError(Error):
    """Вызывается, когда введен не верный знак"""
    pass


class ValueZeroError(Error):
    """Вызывается, когда пытаются делить на 0"""
    pass


def calc():
    try:
        list_signs = ['+', '-', '*', '/']
        sing = input('Введите операцию (+, -, *, / или 0 для выхода):')
        if sing == '0':
            print('До встречи!')
            return
        elif sing not in list_signs:
            raise ValueSingError
        first_number = int(input('Введите первое число:'))
        if first_number == 0 and sing == '/':
            raise ValueZeroError
        second_number = int(input('Введите второе число:'))
        if sing == '+':
            print(first_number + second_number)
            calc()
        elif sing == '-':
            print(first_number - second_number)
            calc()
        elif sing == '*':
            print(first_number * second_number)
            calc()
        elif sing == '/' and first_number != 0:
            print(first_number / second_number)
            calc()
    except ValueZeroError:
        print('На 0 делить нельзя. Попробуйте снова')
        calc()
    except ValueSingError:
        print('Не верный знак! Попробуйте еще раз.')
        calc()
    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь')
        calc()


if __name__ == '__main__':
    calc()

from math import *
while True:
    n = input('Введите число: ')
    try:
        n = float(n)
    except ValueError:
        print('Ошибка: введите число!')
        continue
    operation = input("Выберите операцию из меню: +,-,*,/,^,корень,sin,cos,tg,ctg,факториал; или введите 'стоп' - для завершения работы с калькулятором: ")
    if operation.lower() == 'стоп':
        print('Работа с калькулятором завершена')
        break
    if operation in ['+', '-', '*', '/', '^']:
        n2 = input('Введите второе число: ')
        try:
            n2 = float(n2)
        except ValueError:
            print('Ошибка: введите число!')
            continue
        n2 = float(n2)
        if operation == '+':
            result = n + n2
        elif operation == '-':
            result = n - n2
        elif operation == '*':
            result = n * n2
        elif operation == '/':
            if n2 == 0:
                print('Ошибка: деление на 0!')
                continue
            result = n / n2
        elif operation == '^':
            result = pow(n, n2)

    elif operation.lower() in ['корень', 'sin', 'cos', 'tg', 'ctg', 'факториал']:
        if operation.lower() == 'корень':
            if n < 0:
                print('Ошибка: извлечение корня из отрицательного числа!')
                continue
            result = sqrt(n)
        elif operation.lower() == 'sin':
            units = input("Введите единицу измерения для числа (радианы, градусы): ")
            if units.lower() == 'радианы':
                result = sin(n)
            elif units.lower() == 'градусы':
                result = sin(radians(n))
            else:
                print('Ошибка: неизвестная единица измерения')
                continue
        elif operation.lower() == 'cos':
            units = input("Введите единицу измерения для числа (радианы, градусы): ")
            if units.lower() == 'радианы':
                result = cos(n)
            elif units.lower() == 'градусы':
                result = cos(radians(n))
            else:
                print('Ошибка: неизвестная единица измерения')
                continue
        elif operation.lower() == 'tg':
            units = input("Введите единицу измерения для числа (радианы, градусы): ")
            if units.lower() == 'радианы':
                if round(cos(n)) == 0:
                    print('Ошибка: tg не существует на числах, кратных pi/2 радиан!')
                    continue
                result = round(tan(n))
            elif units.lower() == 'градусы':
                if round(cos(radians(n))) == 0:
                    print('Ошибка: tg не существует на числах, кратных 90 градусам!')
                    continue
                result = round(tan(radians(n)))
            else:
                print('Ошибка: неизвестная единица измерения')
                continue
        elif operation.lower() == 'ctg':
            units = input("Введите единицу измерения для числа (радианы, градусы): ")
            if units.lower() == 'радианы':
                if round(tan(n)) == 0:
                    print('Ошибка: ctg не существует на 0 и числах, кратных pi радиан!')
                    continue
                result = 1 / round(tan(n))
            elif units.lower() == 'градусы':
                if n == 0 or n % 180 == 0:
                    print('Ошибка: ctg не существует на числах, кратных 180 градусам!')
                    continue
                result = 1 / round(tan(radians(n)))
            else:
                print('Ошибка: неизвестная единица измерения')
                continue
        elif operation.lower() == 'факториал':
            if int(n) != n or n < 0:
                print('Ошибка: факториалы определены для натуральных чисел и нуля!')
                continue
            result = factorial(int(n))
    else:
        print('Ошибка: такой операции в меню нет, попробуйте ещё раз!')
        continue
    print('Ваш результат: ', result)
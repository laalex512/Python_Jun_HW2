# Создайте несколько переменных разных типов.
# Проверьте к какому типу относятся созданные переменные
import math


def task1():
    a = 6
    b = "fdh"
    x = True

    print(type(a), type(b), type(x))


# task1()

# -----------------------------------------------------------------
# Создайте в переменной data список значений разных типов перечислив их через
# запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# ✔ порядковый номер начиная с единицы
# ✔ значение
# ✔ адрес в памяти
# ✔ размер в памяти
# ✔ хэш объекта
# ✔ результат проверки на целое число только если он положительный
# ✔ результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

def task2():
    data = [654, "dfhjh", True, 'dfhkjh', 654, 555, 'dfhkjh']

    for index, value in enumerate(data):
        print(index + 1, value, id(value),
              value.__sizeof__(), hash(value), end=" ")
        if isinstance(value, str):
            print("String")
        elif isinstance(value, int):
            print("Integer")


# task2()

# ---------------------------------------------------------------------
# Тут я объединил все задачи с переводом в системы исчисления (можно в любую до 36)

def task3():
    # функция для преобразования числа в соответствующий символ:
    def add_symbol(num: int) -> str:
        START_LETTER = 'a'
        result = ""
        if num > 9:
            result = chr(ord(START_LETTER) + num - 10)
        else:
            result = str(num)
        return result

    number = int(input("введите число: "))
    measure = int(input("В какую систему (до 36)? "))
    test_result = 0
    match measure:
        case 2:
            test_result = bin(number)
        case 8:
            test_result = oct(number)
        case 16:
            test_result = hex(number)

    result = ""
    while number >= measure:
        result += add_symbol(number % measure)
        number = number // measure
    result += add_symbol(number)

    result = result[::-1]

    print(f"Результат:  {result}")
    if test_result:
        print(f"Проверка: {test_result}")


# task3()

# ---------------------------------------------------------------------

# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой


def task4():
    import decimal
    import math

    decimal.getcontext().prec = 42
    diameter = decimal.Decimal(input("Enter diameter(<=1000): "))

    if diameter > 1000 or diameter <= 0:
        print("Incorrect input")
    else:
        _pi = decimal.Decimal(math.pi)
        print(f"length = {_pi * diameter}")
        print(f"square = {_pi * diameter ** 2 / 4}")


# task4()


# ---------------------------------------------------------------------


# Напишите программу, которая решает
# квадратные уравнения даже если
# дискриминант отрицательный.
#  Используйте комплексные числа
# для извлечения квадратного корня.

def task5(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant >= 0:
        root1 = (-b - math.sqrt(discriminant)) / (2 * a)
        root2 = (-b + math.sqrt(discriminant)) / (2 * a)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)

    print(f"Root1: {root1}")
    print(f"Root2: {root2}")


# task5(4, 3, 2)


# ---------------------------------------------------------------------

# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

# ---------------------------------------------------------------------

# Домашние задачи

# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.


# метод ниже переводит в любую систему исчисления до 36
# проверка выводится для 2-, 8- и 16-ричной систем
def home_task1():
    # функция для преобразования числа в соответствующий символ:
    def add_symbol(num: int) -> str:
        START_LETTER = 'a'
        result = ""
        if num > 9:
            result = chr(ord(START_LETTER) + num - 10)
        else:
            result = str(num)
        return result

    number = int(input("введите число: "))
    measure = int(input("В какую систему (до 36)? "))
    check_result = 0
    match measure:
        case 2:
            check_result = bin(number)
        case 8:
            check_result = oct(number)
        case 16:
            check_result = hex(number)

    result = ""
    while number >= measure:
        result += add_symbol(number % measure)
        number = number // measure
    result += add_symbol(number)

    result = result[::-1]

    print(f"Результат:  {result}")
    if check_result:
        print(f"Проверка: {check_result}")


# home_task1()

# ---------------------------------------------------------------------

# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions

def home_task2():
    import fractions
    import math

    def convert_to_digit(input: str) -> tuple[int, int]:
        return int(input.split("/")[0]), int(input.split("/")[1])

    def fraction_sum(numerator1, denominator1, numerator2, denominator2) -> str:
        # наибольшее общее кратное:
        lcm = abs(denominator1 * denominator2) // math.gcd(denominator1, denominator2)
        numerator_result = numerator1 * (lcm // denominator1) + \
                           numerator2 * (lcm // denominator2)
        if math.gcd(lcm, numerator_result) > 1:
            temp = numerator_result
            numerator_result //= math.gcd(lcm, numerator_result)
            lcm //= math.gcd(lcm, temp)
        return f"{str(numerator_result)}/{str(lcm)}"

    def fraction_multiply(numerator1, denominator1, numerator2, denominator2) -> str:
        numerator_result = numerator1 * numerator2
        denominator_result = denominator1 * denominator2
        if math.gcd(denominator_result, numerator_result) > 1:
            temp = numerator_result
            numerator_result //= math.gcd(denominator_result, numerator_result)
            denominator_result //= math.gcd(denominator_result, temp)
        return f"{str(numerator_result)}/{str(denominator_result)}"

    NUM1 = "5/8"
    NUM2 = "4/9"

    fraction1 = convert_to_digit(NUM1)
    fraction2 = convert_to_digit(NUM2)

    sum = fraction_sum(fraction1[0], fraction1[1], fraction2[0], fraction2[1])
    multiply = fraction_multiply(fraction1[0], fraction1[1], fraction2[0], fraction2[1])
    print(f"результат программы (сумма): {sum}")
    print(f"результат программы (произведение): {multiply}")

    check_num1 = fractions.Fraction(fraction1[0], fraction1[1])
    check_num2 = fractions.Fraction(fraction2[0], fraction2[1])
    print(f"проверка на сумму: {check_num1 + check_num2}")
    print(f"проверка на произведение: {check_num1 * check_num2}")

# home_task2()

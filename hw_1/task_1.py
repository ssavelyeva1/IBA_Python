# Даны три числа a, b и c. Найти среднее геометрическое этих чисел, если все они отличны от нуля,
# и среднее арифметическое в противном случае.

a = 1
b = 2
c = 4

if a != 0 and b != 0 and c != 0:
    print('Cреднее геометрическое чисел = ', (a * b * c) ** (1/3))
else:
    print('Cреднее арифметическое чисел = ', (a + b + c) / 3)
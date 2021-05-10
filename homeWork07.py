from random import randint


class ComplexNumber:
    def __init__(self, realPart, imagPart):
        self.realPart = realPart
        self.imagPart = imagPart

    def __str__(self):
        if self.imagPart > 0:
            return f'комплексное число = {self.realPart}+{self.imagPart}i'
        elif self.imagPart == 0:
            return f'комплексное число = {self.realPart}'
        else:
            return f'комплексное число = {self.realPart}{self.imagPart}i'

    def __add__(self, other):
        return ComplexNumber((self.realPart + other.realPart), (self.imagPart + other.imagPart))

    def __sub__(self, other):
        return ComplexNumber((self.realPart - other.realPart), (self.imagPart - other.imagPart))

    def __mul__(self, other):
        return ComplexNumber((self.realPart * other.realPart - self.imagPart * other.imagPart),
                             (self.realPart * other.imagPart + self.imagPart * other.realPart))


print(
    'Комплексные числа будем генерировать (встроенный в Python класс complex не используем по условию задания)')
complexNumberA = ComplexNumber(randint(-10, 10), randint(-10, 10))
complexNumberB = ComplexNumber(randint(-10, 10), randint(-10, 10))
print(complexNumberA)
print(complexNumberB)
print(f'результат сложения: {complexNumberA + complexNumberB}')
print(f'результат вычитания: {complexNumberA - complexNumberB}')
print(f'результат умножения: {complexNumberA * complexNumberB}')

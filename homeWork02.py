class DivisionByZero(Exception):
    def __str__(self):
        return f'Попытка деления на 0'


class Division:
    dividend: float
    divider: float

    def __init__(self, dividend, divider):
        self.dividend = dividend
        self.divider = divider

    def division(self):
        if self.divider == 0:
            raise DivisionByZero()
        else:
            return f'Результат деления {self.dividend} на {self.divider}: {round(self.dividend / self.divider, 4)}'


try:
    userDividend = float(input('Ведите делимое: '))
    userDivider = float(input('Введите делитель: '))
except ValueError:
    exit('Введено не число')
userResult = Division(userDividend, userDivider)
try:
    print(userResult.division())
except DivisionByZero as exception:
    print(exception.__str__())

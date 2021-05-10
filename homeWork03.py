class CheckString(Exception):
    def __init__(self, string):
        self.string = string

    def __str__(self):
        return f'{self.string} не число'


class OnlyNumberAppend:
    numberList: list = []

    def __init__(self, item):
        self.item = item

    def numberAppend(self):
        if self.item.count('.') & (self.item.replace('.', '')).isdigit():
            addNumber = float(self.item)
        elif self.item.isdigit():
            addNumber = int(self.item)
        else:
            raise CheckString(self.item)
        self.numberList.append(addNumber)
        return f'{self.numberList}'


while True:
    item = input('Введите элемент списка (для окончания ввода введите "q + Enter": ')
    if item == 'q':
        break
    else:
        try:
            OnlyNumberAppend(item).numberAppend()
        except CheckString as exception:
            print(f'"{exception.string}" не является числом и в список не добавляется')

print(OnlyNumberAppend.numberList)

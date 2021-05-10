'''
Задание показалось слишком запутанным при жестком ограниченнии по времени,
потому сделано с помощью костылей и не полностью.
'''


class Store:
    techsList: dict = {'Принтер': 0, 'Сканер': 0, 'Копир': 0}

    def __init__(self, typeOfTech):
        self.typeOfTech = typeOfTech

    def receptTech(self, count):
        self.count = count
        if self.typeOfTech == 'Принтер':
            self.techsList['Принтер'] = self.techsList.get('Принтер') + self.count
            return self.techsList

        if self.typeOfTech == 'Сканер':
            self.techsList['Сканер'] = self.techsList.get('Сканер') + self.count
            return self.techsList

        if self.typeOfTech == 'Копир':
            self.techsList['Копир'] = self.techsList.get('Копир') + self.count
            return self.techsList

    def issueTech(self, count):
        self.count = count
        if self.typeOfTech == 'Принтер':
            if self.techsList.get('Принтер') - self.count < 0:
                print(f"НЕВОЗМОЖНО ВЫПОЛНИТЬ! На складе осталось {self.techsList.get('Принтер')} единиц техники")
                return self.techsList
            else:
                self.techsList['Принтер'] = self.techsList.get('Принтер') - self.count
                return self.techsList

        if self.typeOfTech == 'Сканер':
            if self.techsList.get('Сканер') - self.count < 0:
                print(f"НЕВОЗМОЖНО ВЫПОЛНИТЬ! На складе осталось {self.techsList.get('Сканер')} единиц техники")
                return self.techsList
            else:
                self.techsList['Сканер'] = self.techsList.get('Сканер') - self.count
                return self.techsList

        if self.typeOfTech == 'Копир':
            if self.techsList.get('Копир') - self.count < 0:
                print(f"НЕВОЗМОЖНО ВЫПОЛНИТЬ! На складе осталось {self.techsList.get('Копир')} единиц техники")
                return self.techsList
            else:
                self.techsList['Копир'] = self.techsList.get('Копир') - self.count
                return self.techsList


newPrinter = Store('Принтер')
newScaner = Store('Сканер')
newCopier = Store('Копир')

try:
    putPrinter = int(input('Введите приход принтеров на склад: '))
    print(f'Теперь на складе хранятся: {newPrinter.receptTech(putPrinter)}')
    putScanner = int(input('Введите приход сканеров на склад: '))
    print(f'Теперь на складе хранятся: {newScaner.receptTech(putScanner)}')
    putCopier = int(input('Введите приход копировальных аппаратов на склад: '))
    print(f'Теперь на складе хранятся: {newCopier.receptTech(putCopier)}')

    getPrinter = int(input('Введите количество принтеров переданных со склада: '))
    print(f'Теперь на складе хранятся: {newPrinter.issueTech(getPrinter)}')
    getScaner = int(input('Введите количество сканеров переданных со склада: '))
    print(f'Теперь на складе хранятся: {newScaner.issueTech(getScaner)}')
    getCopier = int(input('Введите количество копировальных аппаратов переданных со склада: '))
    print(f'Теперь на складе хранятся: {newCopier.issueTech(getCopier)}')
except ValueError:
    exit('Неверно введены данные!')

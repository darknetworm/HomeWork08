class Data:

    @classmethod
    def extracting(cls, daymonyear):
        try:
            result = [int(item) for item in (daymonyear.split('-'))]
        except ValueError:
            exit('Данные введены неправильно')
        return cls.validation(result)

    @staticmethod
    def validation(result):
        if result[0] not in range(1, 32):
            return f'Дата должна быть в пределах 01-31 в зависимости от месяца'
        elif (result[0] == 31) & (result[1] in [4, 6, 9, 11]):
            return f'В этом месяце не может быть больше 30 дней'
        elif (result[0] in [30, 31]) & (result[1] == 2):
            return f'В феврале может быть либо 28, либо 29 дней (високосность не проверяем)'
        if result[1] not in range(1, 12):
            return f'Месяц может быть в пределах 01-12'
        if len(str(result[2])) != 4:
            return f'Год должен содержать 4 цифры (допотопный времена и далекое будущее не рассматриваем)'
        return f'Все данные введены корректны'


userDay = input('Введите день формате dd: ')
userMonth = input('Введите месяц в формате mm: ')
userYear = input('Введите год в формате yyyy: ')
userData = userDay + '-' + userMonth + '-' + userYear
print(f'Для проверки корректности введенных данных в класс Data передаем строку "{userData}", {type(userData)}')

print(Data.extracting(userData))

from datetime import datetime
from time import strptime


class DatabaseWorker:

    def __init__(self, path):
        self.time = datetime.now().strftime('%d/%m/%Y')
        self.time_ = strptime(self.time, '%d/%m/%Y')
        self.path = path

    def databaseCheck(self, value):
        if value:
            print(self.databaseExtract())
            for data in self.databaseExtract():
                if value in data:
                    try:
                        time_check = strptime(''.join(data[4:5]).replace('.', '/'), '%d/%m/%Y')
                        print(time_check)
                        print('\nСтрока для поиска : %s' % value)
                        print('Список : %s\nСостояние : %s\nДата проверки : %s' % (
                            ', '.join(data), ''.join(data[5:6]), ''.join(data[4:5])))
                        if time_check < self.time_:
                            print(time_check)
                            print('Статус : \x1b[31;3mпросрочено!\033[0m\n')
                        elif time_check > self.time_:
                            print('Статус : \033[32;3mне просрочено!\033[0m\n')
                        else:
                            print('Даты совпадают!\n')
                    except ValueError as err:
                        print('\x1b[31;3mДата указана неправильно! %s\033[0m' % err)
                else:
                    pass
        else:
            for data in self.databaseExtract():
                try:
                    time_check = strptime(''.join(data[4:5]).replace('.', '/'), '%d/%m/%Y')
                    print('\nСтрока для поиска : отсутствует')
                    print('Список : %s\nСостояние : %s\nДата проверки : %s' % (
                        ', '.join(data), ''.join(data[5:6]), ''.join(data[4:5])))
                    if time_check < self.time_:
                        print('Статус : \x1b[31;3mпросрочено!\033[0m\n')
                    elif time_check > self.time_:
                        print('Статус : \033[32;3mне просрочено!\033[0m\n')
                    else:
                        print('Даты совпадают!\n')
                except ValueError as err:
                    print('\x1b[31;3mВремя указано неправильно! %s\033[0m' % err)

    def databaseExtract(self):
        extractedData = list()
        for data in open(self.path, 'r', encoding='utf_8_sig').readlines():
            extractedData.append(data.rstrip('\r\n').rsplit(','))
        return extractedData

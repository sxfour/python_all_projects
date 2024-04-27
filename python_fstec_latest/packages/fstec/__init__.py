from openpyxl import load_workbook
from rich.console import Console
from rich.table import Table


class SearchFstec:

    def __init__(self, path, phrase, width):
        self.path = path
        self.searchData = phrase
        self.set_value = None
        self.index = 0

        self.foundedData = list()
        self.cellCoordinate = list()

        self.workbook = load_workbook(filename=self.path, read_only=True)
        self.worksheet = self.workbook['Sheet']

        self.console = Console(width=width)
        self.table = Table(title='[test] ФСТЭК Уязвимости от 11.01.2023')

    def fstecSearch(self):
        for rows in self.worksheet:
            for cell in rows:
                if self.searchData in str(cell.value):
                    self.foundedData.append(cell.row)
                    self.table.add_row(
                        str(self.index), self.worksheet[f'A{str(cell.row)}'].value,
                        self.worksheet[f'D{str(cell.row)}'].value, self.worksheet[f'B{str(cell.row)}'].value,
                        self.worksheet[f'F{str(cell.row)}'].value, self.worksheet[f'I{str(cell.row)}'].value,
                        self.worksheet[f'S{str(cell.row)}'].value, self.worksheet[f'M{str(cell.row)}'].value,
                        self.worksheet[f'J{str(cell.row)}'].value, self.worksheet[f'R{str(cell.row)}'].value,
                    )
                    self.index += 1
                    print('Строка : ' + str(cell.row), '\nСтолбец : ' + str(cell.column),
                          '\nЯчейка : ' + str(cell.coordinate), '\nЗначение : ' + str(cell.value),
                          '\nСохранённая строка :', self.foundedData, '\n', )
                    break
                else:
                    pass
        if self.foundedData:
            self.console.print(self.table)
            self.set_value = self.foundedData[int(input("\nВыберите ID : "))]
            for rows_ in self.worksheet[f'A{self.set_value}':f'V{self.set_value}']:
                string = ''
                for cell in rows_:
                    self.cellCoordinate.append(cell.coordinate)
                    string = string + str(cell.value) + ' '
                print(string)
                print('\nCoordinates : ', self.cellCoordinate, '\n')
        else:
            print('Ничего не найдено по', self.searchData, 'запрос :', self.foundedData)

    def createTable_fstec(self, justify, fstec_small):
        self.table.add_column('ID', no_wrap=True, justify=justify, width=2)
        for key in fstec_small:
            self.table.add_column(key, no_wrap=True, justify=justify, width=20)
        return self.table

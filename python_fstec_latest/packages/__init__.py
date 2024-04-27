from fstec.settings import fstec_small
from fstec import SearchFstec


def mainMenu():
    find_data = str(input('\nВведите поисковый запрос, используя ключевое слово : '))

    start1 = SearchFstec(path='fstec/test.xlsx', phrase=find_data, width=1920)
    start1.createTable_fstec(justify='center', fstec_small=fstec_small)
    start1.fstecSearch()


if __name__ == '__main__':
    mainMenu()

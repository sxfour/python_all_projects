from packages import DatabaseWorker

if __name__ == '__main__':
    Database = DatabaseWorker(path='packages/databases/base.mts')
    Database.databaseCheck(value=input('\nПоиск по строке : '))

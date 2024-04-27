from IPY.bc import DatabaseWorker

if __name__ == '__main__':
    Database = DatabaseWorker(path='bc/databases/base.txt')
    Database.databaseCheck(value='ООО "Развитие"')

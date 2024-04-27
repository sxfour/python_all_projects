from psycopg2 import connect, DatabaseError
from rich.console import Console
from rich.table import Table


class SearchFstec:

    def __init__(self, data, width, title):
        self.title = title
        self.table = Table(title=self.title, show_footer=False)
        self.console = Console(width=width)
        self.database = data

        self.database_version = None
        self.searchPhrase = None
        self.user_choice = True
        self.section = None
        self.cursor = None
        self.conn = None

    def searchPostgreSQL(self):
        try:
            self.conn = connect(**self.database)
            self.cursor = self.conn.cursor()
            self.cursor.execute('SELECT version()')
            self.database_version = self.cursor.fetchone()

            print('\n[+] Connected to database, version : {0}\n'.format(self.database_version[0]))
            while self.user_choice:
                self.searchPhrase = str(input('(cve) fstec>'))
                if self.searchPhrase == 'help':
                    print('\nТестовая версия поиска уязвимостей по базе ФСТЭК\nПоиск по CVE, например : CVE-2023-21549'
                          '\ndb_info - Информация о подключенной базе данных\nexit - Выход\nhelp - Справка\n')
                elif self.searchPhrase == 'db_info':
                    self.cursor.execute('SELECT * FROM fstec')
                    info = len(self.cursor.fetchall())

                    print('\nБаза данных : {0}\nНайдено записей : {1}\nНастройки .ini : {2}\n'.format(self.database_version[0], info, self.database))
                elif self.searchPhrase == 'exit':
                    self.user_choice = False
                else:
                    self.cursor.execute(f"SELECT * FROM fstec WHERE cve LIKE '{self.searchPhrase}%'")
                    value = self.cursor.fetchall()
                    for data in range(len(value)):
                        self.table.add_row(
                            value[data][0], value[data][1], value[data][2], value[data][3],
                            value[data][4], value[data][5], value[data][6], value[data][7],
                            value[data][8], value[data][9], value[data][10], value[data][11],
                            value[data][12], value[data][13], value[data][14], value[data][15],
                        )
                    self.console.print(self.table)
                    self.resetTable()
        except (Exception, DatabaseError) as err:
            print(err)
        finally:
            if self.conn is None:
                print('\n[!] Re-check correct .ini on local path, data : {0}'.format(self.database))
            elif self.conn is not None:
                self.conn.close()
                print('\n[!] Connection closed')

    def createTable_fstec(self, justify, fstec_sql):
        for key in fstec_sql:
            self.table.add_column(key, no_wrap=True, justify=justify, width=20)
        return self.table

    def resetTable(self):
        self.table = Table(title=self.title, footer_style=None, header_style=None)

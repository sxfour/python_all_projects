from psycopg2 import connect, DatabaseError
from configparser import ConfigParser


class WorkerSQL:

    def __init__(self, get_settings, settings, section):
        self.get_settings = get_settings
        self.filename = settings
        self.section = section

        self.parser = ConfigParser()
        self.database = dict()
        self.data = dict()

        self.connection = None

    def connectPostgreSQL(self):
        try:
            self.connection = connect(**self.databaseCheck())

            cursor = self.connection.cursor()
            cursor.execute(self.get_settings)

            self.data = cursor.fetchall()
            cursor.close()

            # print(self.data)
            return self.data

        except (Exception, DatabaseError) as error:
            print(error)
        finally:
            if self.connection is not None:
                self.connection.close()
                print('\n[+] Запрос : [{0}] выполнен, соединение закрыто...'.format(self.get_settings))
            else:
                print('\n[!] Соединение не установлено...')

    def databaseCheck(self):
        self.parser.read(self.filename)

        if self.parser.has_section(self.section):
            params = self.parser.items(self.section)
            for param in params:
                self.database[param[0]] = param[1]
        else:
            raise Exception('\n[-] Parameter "{0}" not found in the "{1}" file'.format(self.section, self.filename))

        return self.database

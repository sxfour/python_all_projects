# from connector import WorkerSQL
#
# if __name__ == '__main__':
#     settings = 'postgresql/database.ini'
#     section = 'postgresql'
#
#     WorkerSQL("SELECT version(), CURRENT_DATE", settings, section).connectPostgreSQL()
#     WorkerSQL("SELECT * FROM ipy_names WHERE name_user LIKE 'ИП Ларькова%'", settings, section).connectPostgreSQL()

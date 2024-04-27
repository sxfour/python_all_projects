from fstec.settings import fstec_sql, nmap_columns
from configparser import ConfigParser
from port_scan import ScannerNmap
from fstec import SearchFstec


def databaseCheck(filename, section):
    parser = ConfigParser()
    parser.read(filename)

    database = dict()
    if parser.has_section(section):
        parameters = parser.items(section)
        for parameter in parameters:
            database[parameter[0]] = parameter[1]
    else:
        raise Exception('Parameter "{0}" not found in the "{1}" file'.format(section, filename))

    return database


def mainMenu(host, port, width, filename, section, title):
    # start = ScannerNmap(host=host, port=port, width=width)
    # start.createTable_nmap(justify='right', columns=nmap_columns)
    # start.rollingScan()

    start1 = SearchFstec(data=databaseCheck(filename, section), width=width, title=title)
    start1.createTable_fstec(justify='center', fstec_sql=fstec_sql)
    start1.searchPostgreSQL()


if __name__ == '__main__':
    mainMenu(
        host='192.168.0.110',
        port='22-443',
        width=1920,
        filename='postgresql/database.ini',
        section='postgresql',
        title='[TEST vers. POSTGRESQL] ФСТЭК Уязвимости',
    )

from config import config
import psycopg2


def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('\nConnecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('\nPostgreSQL database version : ')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

        # find info in database
        print('\nSome info in table : ')
        cur.execute("SELECT * FROM fstec WHERE base_id LIKE 'BDU:2022%'")

        db_info_tab = cur.fetchone()
        print(db_info_tab[0:16])

        # close the communication with the PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('\nDatabase connection closed')


if __name__ == '__main__':
    connect()


import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def create_credentials(conn, creds):
    """
    Create a new task
    :param conn:
    :param creds:
    :return:
    """

    sql = ''' INSERT INTO credentials (username, website, password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, creds)
    conn.commit()
    return cur.lastrowid


def main():
    database = r"pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS credentials (
                                        cred_id integer PRIMARY KEY AUTOINCREMENT,
                                        username text NOT NULL,
                                        website text NOT NULL,
                                        password text NOT NULL
                                    ); """

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create credentials table
        create_table(conn, sql_create_projects_table)

    else:
        print("Error! cannot create the database connection.")

def clear_password_db(conn):
    """
    Delete all rows in the tasks table
    :param conn: Connection to the SQLite database
    :return:
    """
    sql = 'DELETE FROM credentials'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()

main()

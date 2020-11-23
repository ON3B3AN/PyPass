import sqlite3
from sqlite3 import Error
from encryptDecrypt import decrypt_passwords
from termcolor import colored


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
        print(colored(e, "red", attrs=['bold']))

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
        print(colored(e, "red", attrs=['bold']))


def create_credentials(conn, creds):
    """
    Create a new task
    :param conn:
    :param creds:
    :return:
    """

    sql = ''' INSERT INTO credential (username, website, password)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, creds)
    conn.commit()
    return cur.lastrowid


def select_all_credentials():
    """
    Query tasks by priority
    :param conn: the Connection object
    :return:
    """
    conn = create_connection("pythonsqlite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM credential")

    rows = cur.fetchall()
    print("")
    for row in rows:
        decrypt_passwords(row)


def clear_password_db():
    """
    Delete all rows in the tasks table
    :return:
    """
    decision = input(colored("Warning! If Credential Dictionary already exists, then all saved websites, usernames, and passwords will be deleted!\n", "yellow", attrs=["bold"]) +
                     "Are you sure you want to do this? (y/n) ")
    loopStop = False
    while not loopStop:
        if decision == "Y" or decision == "y":
            database = r"pythonsqlite.db"
            conn = create_connection(database)
            sql = 'DELETE FROM credential'
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            print(colored("\nCredential Dictionary has been cleared!", "green", attrs=["bold"]))
            loopStop = True
            return True
        else:
            break
            return False


def main():
    database = r"pythonsqlite.db"

    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS credential (
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
        print(colored("Error! cannot create the database connection.", "red", attrs=['bold']))


main()

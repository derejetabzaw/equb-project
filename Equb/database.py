import sqlite3
from sqlite3 import Error
 
# def adapt_array(arr):
#     """
#     http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
#     """
#     out = io.BytesIO()
#     np.save(out, arr)
#     out.seek(0)
#     return sqlite3.Binary(out.read())

# def convert_array(text):
#     out = io.BytesIO(text)
#     out.seek(0)
#     return np.load(out)

 
def create_connection(db_file):
    """ create a database connection to a SQLite database """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        # print(sqlite3.version)
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
 
def create_database_and_tables(database):
    
    # Converts np.array to TEXT when inserting
    # sqlite3.register_adapter(np.ndarray, adapt_array)

    # Converts TEXT to np.array when selecting
    # sqlite3.register_converter("array", convert_array)

    sql_create_equb_table = """ CREATE TABLE IF NOT EXISTS Equb (
                            seed INTEGER NOT NULL,
                            name VARCHAR(40) NOT NULL,
                            lastname VARCHAR(40) NOT NULL,
                            commitment VARCHAR(40) NOT NULL,
                            week INTEGER,
                            hsum INTEGER
                        ); """
    sql_create_basic_information = """ CREATE TABLE IF NOT EXISTS basic_informations (
                            grand_total INTEGER NOT NULL,
                            first_date text NOT NULL
                        ); """
    
    sql_create_view_status = """ CREATE TABLE IF NOT EXISTS view_status (
                            count INTEGER NOT NULL,
                            rounds INTEGER NOT NULL
                        ); """
                                    



    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
 
        # create tasks table
        create_table(conn, sql_create_equb_table)
        create_table(conn,sql_create_basic_information)
        create_table(conn,sql_create_view_status)


    else:
        print("Error! cannot create the database connection.")


def create_information(conn, information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO basic_informations(grand_total,first_date)
              VALUES(?,datetime(?)) '''
    cur = conn.cursor()
    cur.execute(sql, information)
    return cur.lastrowid



def insert_date_and_amount(database,grand_total,date):
        # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = grand_total,date
        create_information(conn, information)




def select_date_from_database(database):

    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT date(first_date) FROM basic_informations")
    #cur.execute("SELECT * FROM video_fingerprint_information")

    rows = cur.fetchall()
    return rows 




def prepare_add_information(conn, information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO view_status(count,rounds)
              VALUES(?,?) '''
    cur = conn.cursor()
    cur.execute(sql, information)
    return cur.lastrowid



def insert_round_and_count(database,count,rounds):
        # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = count,rounds
        prepare_add_information(conn, information)




def select_count_from_database(database):

    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT count FROM view_status")

    rows = cur.fetchall()
    return rows 



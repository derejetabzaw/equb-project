import sqlite3
from sqlite3 import Error
import numpy as np 
import io 
 
def adapt_array(arr):
    """
    http://stackoverflow.com/a/31312102/190597 (SoulNibbler)
    """
    out = io.BytesIO()
    np.save(out, arr)
    out.seek(0)
    return sqlite3.Binary(out.read())

def convert_array(text):
    out = io.BytesIO(text)
    out.seek(0)
    return np.load(out,allow_pickle=True)

 
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
    sqlite3.register_adapter(np.ndarray, adapt_array)

    # Converts TEXT to np.array when selecting
    sqlite3.register_converter("array", convert_array)

    sql_create_equb_table = """ CREATE TABLE IF NOT EXISTS Equb (
                            name text NOT NULL,
                            lastname text NOT NULL,
                            rowposition INTEGER,
                            columncount INTEGER,
                            currentrow INTEGER,
                            currentcolumn INTEGER

                        ); """
    sql_create_basic_information = """ CREATE TABLE IF NOT EXISTS basic_informations (
                            grand_total INTEGER NOT NULL,
                            first_date text NOT NULL
                        ); """
    
    sql_create_view_status = """ CREATE TABLE IF NOT EXISTS view_status (
                            count INTEGER NOT NULL,
                            rounds INTEGER NOT NULL
                        ); """
    sql_create_amount = """ CREATE TABLE IF NOT EXISTS Amount (
                            file STRING,
                            amount INTEGER NOT NULL,
                            currentrow INTEGER,
                            currentcolumn INTEGER,
                            checked_box  array,
                            cheque_information array,
                            checkbox_bank_options array,
                            others_text text
                        ); """
    sql_create_save_table = """ CREATE TABLE IF NOT EXISTS SAVE (
                            name text,
                            lastname text,
                            commitment varchar,
                            amount integer,
                            rounds integer,
                            currentrow integer,
                            currentcolumn integer,
                            rowcount integer,
                            columncount integer
                        ); """
                                    



    # create a database connection
    conn = create_connection(database)
    # create tables
    if conn is not None:
 
        # create tasks table
        create_table(conn, sql_create_equb_table)
        create_table(conn,sql_create_basic_information)
        create_table(conn,sql_create_view_status)
        create_table(conn,sql_create_amount)
        create_table(conn,sql_create_save_table)


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

def select_equb_amount_from_database(database):

    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT grand_total FROM basic_informations")
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



def add_name_and_last_name(conn, information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Equb(name,lastname,rowposition,columncount,currentrow,currentcolumn)
              VALUES(?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, information)
    return cur.lastrowid



def insert_data_entry(database,name,lastname,rowcount,columncount,currentRow,currentColumn):
    # create a database connection
    conn = create_connection(database)
    with conn:
        # tasks
        information = name,lastname,rowcount,columncount,currentRow,currentColumn
        add_name_and_last_name(conn, information)



def select_equb_information(database):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT * FROM Equb")
    rows = cur.fetchall()
    return rows 


def add_amount(conn, information):
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' INSERT INTO Amount(file,amount,currentrow,currentcolumn,checked_box,cheque_information,checkbox_bank_options,others_text)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, information)
    return cur.lastrowid




def insert_amount_dialog(database,file,amount,currentrow,currentcolumn,checked_box,cheque_information,checkbox_bank_options,others_text):
    conn = create_connection(database)
    with conn:
        information = file,amount,currentrow,currentcolumn,adapt_array(checked_box),adapt_array(cheque_information),adapt_array(checkbox_bank_options),others_text
        add_amount(conn, information)


def select_amount(database,row,column,filename):
    conn = create_connection(database)
    cur = conn.cursor()
    cur.execute("SELECT amount,checked_box,cheque_information,checkbox_bank_options,others_text FROM Amount WHERE currentrow = ? AND currentcolumn=? AND file = ?",(row,column,filename))
    rows = cur.fetchall()
    return rows

# def select_all_information(database,file):
#     conn = create_connection(database)
#     cur = conn.cursor()
#     cur.execute("SELECT amount,checked_box,cheque_information,checkbox_bank_options,others_text FROM Amount WHERE filename = ? ",(file))
#     rows = cur.fetchall()
#     return rows



def save_information(conn,information):
    sql = ''' INSERT INTO SAVE(name,lastname,commitment,amount,rounds,currentrow,currentcolumn,rowcount,columncount)
              VALUES(?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, information)
    return cur.lastrowid

def insert_views_information(database,name,lastname,commitment,amount,rounds,currentrow,currentcolumn,rowcount,columncount):
    conn = create_connection(database)
    with conn:
        information = name,lastname,commitment,amount,rounds,currentrow,currentcolumn,rowcount,columncount
        save_information(conn, information)

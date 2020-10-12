import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ Create a connection to the SQLite database
    :param db_file: database file
    :return: Either a Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        cur = conn.cursor()
        cur.execute(create_table_sql)
    except Error as e:
        print(e)


def insert_recipe(conn, recipe):
    sql = """INSERT INTO recipes (name, category, ingredients) VALUES (?, ?, ?) """
    cur = conn.cursor()
    cur.execute(sql, recipe)
    conn.commit()
    return cur.lastrowid


def update_recipe(conn, recipe):
    sql = """UPDATE recipes 
             SET name = ?,
                 category = ?,
                 ingredients = ?
             WHERE id = ?
    """
    cur = conn.cursor()
    cur.execute(sql, recipe)
    conn.commit()


def select_all_recipes(conn):
    sql = "SELECT * FROM recipes"
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    return rows


def select_by_category(conn, category):
    sql = "SELECT * FROM recipes WHERE category=?"
    cur = conn.cursor()
    cur.execute(sql, (category,))
    rows = cur.fetchall()
    for row in rows:
        print(row)


def select_random_week(conn, chosen_options):
    cur = conn.cursor()
    if "Takeout" in chosen_options:
        try:
            day = int(input("What day would you like to eat takeout? Please select the day number. [12345] "))
        except:
            print("The day number chosen was not a number.")
        sql = "SELECT * FROM recipes WHERE id IN (SELECT id FROM recipes ORDER BY RANDOM() LIMIT 4)"
        cur.execute(sql)
        rows = cur.fetchall()
        rows.insert(day - 1, "Takeout")
    else:
        sql = "SELECT * FROM recipes WHERE id IN (SELECT id FROM recipes ORDER BY RANDOM() LIMIT 5)"
        cur.execute(sql)
        rows = cur.fetchall()
    return rows


def main():
    # database = "recipes.db"
    database = ":memory:"

    sql_create_recipes_table = """CREATE TABLE IF NOT EXISTS recipes (
                                        id integer PRIMARY KEY,
                                        name text,
                                        category text,
                                        ingredients text
                                );"""

    conn = create_connection(database)                                

    if conn is None:
        print("Cannot create connection to database.")
    else:
        with conn:
            create_table(conn, sql_create_recipes_table)
            select_all_recipes(conn)

            
    
    

if __name__ == "__main__":
    main()
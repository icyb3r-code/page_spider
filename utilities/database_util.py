import sqlite3 as lite
from utilities.bcolors import bcolors



def create_database(databse_path: str):
    conn = lite.connect(databse_path)
    with conn:
        cur = conn.cursor()
        cur.execute("drop table if exists words")
        ddl = "CREATE TABLE words (word	TEXT NOT NULL UNIQUE,usage_count INTEGER NOT NULL DEFAULT 1, PRIMARY KEY(word))"
        cur.execute(ddl)
    conn.close()


def save_words_2_databsae(database_path: str, words_list: list):
    green = f"{bcolors.OKGREEN}[!]{bcolors.ENDC} "
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        for word in words_list:
            # check if the word is in the database
            sql = "select count(word) from words where word='{}'".format(word)
            cur.execute(sql)
            count = cur.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count = usage_count + 1 where word = '{}'".format(word)
                cur.execute(sql)
            else:
                sql = "insert into words(word) values ('{}')".format(word)
                cur.execute(sql)
        cur.close()
        print (f"{green} Database save completed!")


def fetch_n_rows(database_path: str,n_rows: int):
    conn = lite.connect(database_path)
    with conn:
        cur = conn.cursor()
        sql = "select * from words order by usage_count desc LIMIT {}".format(n_rows)
        cur.execute(sql)
        top5 = cur.fetchall()
        max_n =max(len(sublist[0]) for sublist in top5)
        indent = max_n + 3
        for word in top5:
            space = " "*(indent - len(word[0]))
            print(f"\t[*] {word[0]}{space}{word[1]}")

def top_n_rows(database_path: str,top_n: int):
    if top_n > 15:
        fetch_n_rows(database_path,15)
    elif top_n <= 15 and top_n >=1:
        fetch_n_rows(database_path,top_n)
    else:
        pass


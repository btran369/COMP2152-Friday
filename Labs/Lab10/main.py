import sqlite3
from contextlib import closing

try:
    with closing(sqlite3.connect('test.db')) as db_connection:
        db_connection.row_factory = sqlite3.Row
        with closing(db_connection.cursor()) as cursor:
            try:
                query1 = "SELECT * FROM demo WHERE ID > 14"
                cursor.execute(query1)
                rows = cursor.fetchall()
                for row in rows:
                    print(row["name"])
            except Exception as e:
                print("Error Executing Query 1")
            
            try:
                del_row = int(input("Enter the row ID threshold for deletion:   "))
                query2 = "DELETE FROM demo WHERE ID < ?"
                cursor.execute(query2, (del_row,))
                num_rows = cursor.rowcount
                print(f"{num_rows} rows affected")
                db_connection.commit()
            except Exception as e:
                print("Error Executing Query 2")
except sqlite3.Error as e:
    print("Failed Connection to database")

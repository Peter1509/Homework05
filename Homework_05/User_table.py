from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("BlogDB_main.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS User(
                UserId integer primary key autoincrement, 
                Username text UNIQUE,
                Mailadress text UNIQUE,
                FirstName text,
                LastName text,
                Birthday real, 
                Password text);
            """)

username = "Son_of_Odin"
mailadresse = "Thor@walhalla.de"
firstname = "Thor"
lastname = "Who_Knows"
birthday = "01.01.0000"
password = "Passwort1234"

db.execute("""
            INSERT INTO USER (Username, Mailadress, FirstName, LastName, Birthday,Password) 
            VALUES (?, ?, ?, ?, ? ,?)
            """, 
            (username, mailadresse, firstname, lastname, birthday, password))

db.pretty_print ("SELECT * FROM USER")
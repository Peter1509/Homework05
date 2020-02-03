from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("BlogDB_main.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS Posts_Default(
                PostDefaultId integer primary key autoincrement, 
                PostName text,
                PostText text);
            """)

postname = "Hallo an Alle"
posttext = "Grüße aus Walhalla. Wer hat noch lust auf eine Schlacht?"


db.execute("""
            INSERT INTO POSTS_DEFAULT (PostName, PostText) 
            VALUES (?, ?)
            """, 
            (postname, posttext))

db.pretty_print ("SELECT * FROM POSTS_DEFAULT")
from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("BlogDB_main.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS Posts_Admin(
                PostAdminId integer primary key autoincrement, 
                PostName text,
                PostText text);
            """)

postname = "Hallo an alle"
posttext = "Grüße aus Walhalla. Wer hat noch lust auf eine Schlacht?"

db.execute("""
            INSERT INTO Posts_Admin (PostName, PostText) 
            VALUES (?, ?)
            """, 
            (postname, posttext))

           
db.pretty_print ("SELECT * FROM Posts_Admin")



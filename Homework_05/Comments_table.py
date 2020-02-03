import sqlite3

db = sqlite3.connect("BlogDB_main.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS Comments(
                CommentId integer primary key autoincrement, 
                CommentText text,
                CommentTime datetime);
            """)

commenttext = "Schlacht klingt super. Bin dabei!"
commenttime = db.execute("SELECT DATETIME()")

db.execute("""
            INSERT INTO COMMENTS (CommentText,CommentTime) 
            VALUES (?, ?)
            """, 
            (commenttext, commenttime))

db.pretty_print ("SELECT * FROM Comments")
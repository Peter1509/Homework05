from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("BlogDB_main.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS Posts(
                PostId integer primary key autoincrement,
                UserId integer,
                PostDefaultId integer,
                PostAdminId integer, 
                CommentId integer,
                PostImageId integer);
            """)

userid = "1"
postdefaultid = ""
postadminid = "1"
commentid = ""
postimageid = ""


db.execute("""
            INSERT INTO POSTS (UserId, PostdefaultId, PostAdminId, CommentId, PostImageId) 
            VALUES (?, ?, ?, ?, ?)
            """, 
            (userid, postdefaultid, postadminid, commentid, postimageid))

db.pretty_print ("SELECT * FROM POSTS")
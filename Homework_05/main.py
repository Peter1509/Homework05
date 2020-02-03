from smartninja_sql.sqlite import SQLiteDatabase

db = SQLiteDatabase("BlogDB_main.sqlite")

db.execute("""CREATE TABLE IF NOT EXISTS User(
                UserId integer primary key autoincrement, 
                Username text,
                Mailadress text UNIQUE,
                FirstName text,
                LastName text,
                Birthday real, 
                Password text);
            """)

db.pretty_print("SELECT * FROM User;")


db.execute("""CREATE TABLE IF NOT EXISTS Posts(
                PostId integer primary key autoincrement,
                UserId integer,
                PostDefaultId integer,
                PostAdminId integer, 
                CommentId integer,
                PostImageId integer);
            """)

db.pretty_print("SELECT * FROM Posts;")

db.execute("""CREATE TABLE IF NOT EXISTS Posts_Default(
                PostDefaultId integer primary key autoincrement, 
                PostName text,
                PostText text);
            """)

db.pretty_print("SELECT * FROM Posts_Default;")

db.execute("""CREATE TABLE IF NOT EXISTS Posts_Admin(
                PostAdminId integer primary key autoincrement, 
                PostName text,
                PostText text);
            """)

db.pretty_print("SELECT * FROM Posts_Admin;")

db.execute("""CREATE TABLE IF NOT EXISTS Comments(
                CommentId integer primary key autoincrement, 
                CommentText text);
            """)

db.pretty_print("SELECT * FROM Comments;")

db.execute("""CREATE TABLE IF NOT EXISTS Post_Image(
                PostImageId integer primary key autoincrement, 
                ImageId integer);
            """)

db.pretty_print("SELECT * FROM Post_Image;")

db.execute("""CREATE TABLE IF NOT EXISTS Images(
                ImageId integer primary key autoincrement, 
                Imagetyp text);
            """)

db.pretty_print("SELECT * FROM Images;")



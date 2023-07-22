from mysql.connector import *
import os

# environment variable for database password
# export SQL_PASS ='your_db_pass'git 
# cd backend && pip install requirements.txt
# run the app from backend/app with uvicorn main:app

class Post:
    def __init__(self, title, content) -> None:
        self.title = title
        self.content = content


mock_posts = [
    Post("Test Post 1", "<h1>Post 1</h1>"),
    Post("Test Post 2", "<h1>Post 2</h1>"),
    Post("Test Post 3", "<h1>Post 3</h1>"),
    Post("Test Post 4", "<h1>Post 4</h1>"),
]


class DatabaseManager:
    def __init__(self) -> None:
        self.mydb = connect(
            host="localhost",
            user="root",
            password=os.environ["SQL_PASS"],
            database="posts",
        )
        cursor = self.get_cursor()

        cursor.execute("DROP TABLE IF EXISTS posts")
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS posts (id int NOT NULL AUTO_INCREMENT, title varchar(255), content varchar(255), PRIMARY KEY (id));"
        )

        self.mydb.commit()
        self.pre_populate_mock_data()

    def pre_populate_mock_data(self):
        for post in mock_posts:
            self.add_post(post)

    def add_post(self, post):
        cursor = self.get_cursor()
        sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
        val = (post.title, post.content)
        cursor.execute(sql, val)
        self.mydb.commit()
        return cursor.lastrowid

    def get_post(self, id):
        if type(id) is not int:
            raise Exception("Not an integer id")
        cursor = self.get_cursor()
        sql = f"SELECT * from posts WHERE id = {id}"
        cursor.execute(sql)
        post = cursor.fetchone()
        return post

    def get_posts(self):
        cursor = self.get_cursor()
        sql = "SELECT * from posts"
        cursor.execute(sql)
        posts = cursor.fetchall()
        return posts

    def update_post(self, post):
        cursor = self.get_cursor()
        sql = "UPDATE posts SET title = %s , content = %s WHERE id = %s"
        val = (post.title, post.content, post.id)
        cursor.execute(sql, val)
        self.mydb.commit()
        if cursor.rowcount > 0:
            return post
        return None

    def delete_post(self, id):
        cursor = self.get_cursor()
        sql = f"DELETE FROM posts WHERE id = {id}"
        cursor.execute(sql)
        self.mydb.commit()
        if cursor.rowcount > 0:
            return id
        return None

    def get_cursor(self):
        return self.mydb.cursor()


# update example
# manager.update_post({"title": "something", "content": "something", "id": 1})
# add example
# manager.add_post({"title": "nothing", "content": "nothing"})

# delete example
# manager.delete_post(1)
# manager.delete_post(2)

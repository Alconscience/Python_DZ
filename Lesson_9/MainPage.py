from sqlalchemy import create_engine
from sqlalchemy.sql import text

class MainPage:

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

# Выполнение запроса на вставку данных в таблицу users

    def test_create_user(self, id, email, subject_id):
        u_create = text("insert into users values (:id, :email, :subject_id)")
        rows = self.db.execute(u_create, id = id, email = email, subject_id = subject_id)
        return rows
               
# Выполнение запроса на редактирование данных в таблице users

    def test_update_user(self, id, email):
        u_update = text("update users set user_email = :email where user_id = :id")
        rows = self.db.execute(u_update, id = id, email = email)
        return rows

# Выполнение запроса на удаление данных в таблице users

    def test_delete_user(self, id):
        u_delete = text("delete from users where user_id = :id")
        rows = self.db.execute(u_delete, id = id)
        return rows

# Выполнение запроса на просмотр данных в таблице users по id

    def test_get_user(self, id):
        u_get = text("select user_id, user_email, subject_id from users where user_id = :id")
        rows = self.db.execute(u_get, id = id)
        return rows
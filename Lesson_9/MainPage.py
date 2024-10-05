from sqlalchemy import create_engine
from sqlalchemy.sql import text

class MainPage:

    def __init__(self, db_connection_string):
        self.db = create_engine(db_connection_string)

# Выполнение запроса на вставку данных в таблицу users

    def test_create_user(self, id, email, subject_id):
        u_create = text("insert into users values (:u_id, :u_email, :s_id)")
        rows = self.db.execute(u_create, u_id=id, u_email=email, s_id=subject_id)
        return rows

# Выполнение запроса на редактирование данных в таблице users

    def test_update_user(self, id, email):
        u_update = text("update users set user_email = :u_email where user_id = :u_id")
        rows = self.db.execute(u_update, u_id=id, u_email=email)
        return rows

# Выполнение запроса на удаление данных в таблице users

    def test_delete_user(self, id):
        u_delete = text("delete from users where user_id = :u_id")
        rows = self.db.execute(u_delete, u_id = id)
        return rows

# Выполнение запроса на просмотр данных в таблице users по id

    def test_get_user(self, id):
        u_get = text("select user_id, user_email, subject_id from users where user_id = :u_id")
        rows = self.db.execute(u_get, u_id = id)
        return rows
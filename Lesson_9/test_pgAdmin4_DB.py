from sqlalchemy import create_engine
from sqlalchemy.sql import text
from MainPage import MainPage

db_conection_string = 'postgresql://postgres:123@localhost:5432/postgres'

def test_DB():
    mainpage = MainPage(db_conection_string)

    # Создание записи в таблице users
    mainpage.test_create_user(99999, '99999@gmail.com', 1)

    # Просмотр записи в таблице users по id
    mainpage.test_get_user(99999)

    # Редактирование записи в таблице users
    mainpage.test_update_user(99999, '12345@gmail.com')

    # Просмотр записи в таблице users по id
    mainpage.test_get_user(99999)

    # Удаление записи в таблице users по id 
    mainpage.test_delete_user(99999)



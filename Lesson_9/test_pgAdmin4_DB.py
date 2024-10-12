from MainPage import MainPage

db_conection_string = 'postgresql://postgres:123@localhost:5432/postgres'

# Создание записи в таблице users
def test_create_user_in_DB():
    mainpage = MainPage(db_conection_string)
    mainpage.test_create_user(99999, '99999@gmail.com', 1)

# Просмотр записи в таблице users по id
def test_get_user_in_DB():
    mainpage = MainPage(db_conection_string)
    mainpage.test_get_user(99999)
     
# Редактирование записи в таблице users
def test_update_user_in_DB():
    mainpage = MainPage(db_conection_string)
    mainpage.test_update_user(99999, '12345@gmail.com')

# Просмотр записи в таблице users по id
def test_get_user_in_DB():
    mainpage = MainPage(db_conection_string)
    mainpage.test_get_user(99999)

# Удаление записи в таблице users по id 
def test_delete_user_in_DB():
    mainpage = MainPage(db_conection_string)
    mainpage.test_delete_user(99999)

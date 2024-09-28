import requests

class EmployeeApi:

    def __init__(self, url):
        self.url = url

# Получение токена
    def get_token(self, user='tecna', password='tecna-fairy'):
        creds = {
            'username': user,
            'password': password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

# Добавление нового сотрудника    
    def create_employee(
            self, company_id, first_name, last_name, email, isActive, id=1,
            middle_name='', url='', phone='',
            birthdate='1985-06-12T11:19:37.153Z'):
        creds = {
            'id': id,
            'firstName': first_name,
            'lastName':  last_name,
            'middleName': middle_name,
            'companyId': company_id,
            'email': email,
            'url': url,
            'phone': phone,
            'birthdate': birthdate,
            'isActive': isActive
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()
        resp = requests.post(
            self.url + '/employee', headers=my_headers, json=creds)
        return resp.json()

# Проверка что есть сотрудники    
    def get_list_employee(self, params_to_add):
        resp = requests.get(self.url + '/employee', params=params_to_add)
        return resp.json()

# Получение данных о сотруднике по id    
    def get_employee_by_id(self, emp_id):
        resp = requests.get(self.url + '/employee/' + str(emp_id))
        return resp.json()

# Изменение информации о сотруднике    
    def change_info_employee(
            self, emp_id, new_last_name, new_url, new_is_active):
        cred = {
            'lastName': new_last_name,
            'url': new_url,
            'isActive': new_is_active
        }
        my_headers = {}
        my_headers["x-client-token"] = self.get_token()

        resp = requests.patch(
            self.url + '/employee/' + str(emp_id), headers=my_headers,
            json=cred)
        return resp.json()

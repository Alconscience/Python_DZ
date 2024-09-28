from EmployeeApi import EmployeeApi
from CompanyApi import CompanyApi

base_url = 'https://x-clients-be.onrender.com'

emp = EmployeeApi(base_url)
com = CompanyApi(base_url)

first_name = "Alexandr"
last_name = "Sviridov"
email = "gprd.san@gmail.com"
middle_name = "Male"
is_active = True
id = 1
phone = "+79876543211"
birthdate = "1985-06-12T11:19:37.153Z"
url = "www.leningrad.ru"

new_last_name = "Ivanov"
new_url = "www.ddt.com"
new_is_active = False

def test_create_employee():
   
    # создание новой компании
    new_company = com.create_company('Company for new employee')
    company_id = new_company["id"]

    # проверка что у созданной компании нет сотрудников
    emp_list_f = emp.get_list_employee(params_to_add={'company': company_id})
    len_before = len(emp_list_f)
    assert len(emp_list_f) == 0

    # создание нового сотрудника
    new_emp = emp.create_employee(
        company_id, first_name, last_name, email, is_active,
        id, middle_name, url, phone, birthdate)
    id_new_emp = new_emp["id"]
    assert len(new_emp) == 1

    # проверка, что создан 1 сотрудник
    emp_list_a = emp.get_list_employee(params_to_add={'company': company_id})
    len_after = len(emp_list_a)
    assert len_after - len_before == 1

    # проверка созданного сотрудника
    new_emp_result = emp.get_employee_by_id(id_new_emp)

    # проверка полей
    assert new_emp_result["id"] == id_new_emp
    assert new_emp_result["firstName"] == first_name
    assert new_emp_result["lastName"] == last_name
    assert new_emp_result["isActive"] is True
    assert new_emp_result["middleName"] == middle_name
    assert new_emp_result["avatar_url"] == url
    assert new_emp_result["phone"] == str(phone)
    assert new_emp_result["birthdate"] == '1985-06-12'

    # Изменение информации о сотруднике    
    edit_emp = emp.change_info_employee(id_new_emp, new_last_name, new_url, new_is_active)

    # проверка измененного сотрудника
    new_edit_result = emp.get_employee_by_id(id_new_emp)

    # проверка полей после изменения информации о сотруднике
    assert new_edit_result["lastName"] == new_last_name
    assert new_edit_result["isActive"] is False
    assert new_edit_result["avatar_url"] == new_url
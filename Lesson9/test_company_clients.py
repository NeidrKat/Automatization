from CompanyAPI import ApiEmployee
from Company import Company
from CompanyBD import DbEmployee

db = DbEmployee("postgresql://x_clients_user:95PM5lQE0NfzJWDQmLjbZ45ewrz1fLYa@dpg-cqsr9ulumphs73c2q40g-a.frankfurt-postgres.render.com/x_clients_db_fxd0")

company = Company("https://x-clients-be.onrender.com")
param_id = "?company=" + str(company.get_id_company())
company_id = company.get_id_company()

api = ApiEmployee("https://x-clients-be.onrender.com")

body = {
    "id": 1,
    "first_name": "string",
    "last_name": "string",
    "middle_name": "string",
    "companyId": company_id,
    "email": "new@gmail.com",
    "employee_url": "url1.com",
    "phone": "string",
    "birthdate": "2000-06-07T08:06:30.137Z",
    "is_active": True
    }


def test_get_list_employee2():
    api_result = api.get_list_employee2(param_id)
    api_result = api_result.json()
    db_result = db.get_list_employee(company_id)
    assert len(api_result) == len(db_result)


def test_add_employee2():
    db_result = db.get_list_employee(company_id)
    api.add_new_employee2(body)
    api_response = api.get_list_employee2(param_id)
    api_response = api_response.json()
    assert len(api_response)-len(db_result) == 1


def test_get_new_employee2():
    resp = api.get_list_employee2(param_id)
    api_new_employee = resp.json()[-1]['id']
    db_new_employee = db.get_id_new_employee()
    assert api_new_employee == db_new_employee


def test_create_employee():
    db.add_new_employee("Гарри", "Поттер",
                        "Мальчик, который выжил",
                        "0987654321", True, company_id)
    data_employee = api.get_new_employee2(db.get_id_new_employee())
    data_employee = data_employee.json()
    assert data_employee["first_name"] == "Гарри"
    assert data_employee["last_name"] == "Поттер"
    assert data_employee["middle_name"] == "Поттер"
    assert data_employee["phone"] == "0987654321"
    assert data_employee["isActive"] is True
    assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    db.delete(id)


def test_edit_employee():
    db.add_new_employee("Гарри", "Поттер",
                        "Мальчик, который выжил",
                        "0987654321", True, company_id)
    id = db.get_id_new_employee()
    db.edit_employee("Добби", "С носком",
                     "Домовой эльф",
                     "0987654321", True, company_id, id)
    data_employee = api.get_new_employee2(id)
    data_employee = data_employee.json()
    assert data_employee["first_тame"] == "Добби"
    assert data_employee["last_тame"] == "С носком"
    assert data_employee["middle_name"] == "Домовой эльф"
    assert data_employee["phone"] == "0987654321"
    assert data_employee["isActive"] is True
    assert data_employee["companyId"] == company_id
    id = db.get_id_new_employee()
    db.delete(id)

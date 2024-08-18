from API import API

api = API("https://x-clients-be.onrender.com")


def test_add_new_employee():
    # Создать новую компанию

    name = "Где-то на затворках головного мозга"
    descr = "твои забытые фейлы"
    result = api.create_company(name, descr)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # получить список сотрудников
    body = api.get_employees_list(companyId)
    len_before = len(body)

    # добавить нового сотрудника
    firstName = "Серое вещ-во"
    lastName = "Правого полушария"
    middleName = "Лобной доли"
    email = "brainRaight@mail.ru"
    url = "string"
    phone = "865423175266"
    birthdate = "2024-08-09"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName,
                                       companyId, email, url, phone, birthdate,
                                       isActive)
    emp_id = new_employee["id"]

    # получить список сотрудников новой компании
    body = api.get_employees_list(companyId)
    len_after = len(body)
    assert len_after - len_before == 1
    assert body[-1]["firstName"] == "Серое вещ-во"
    assert body[-1]["lastName"] == "Правого полушария"
    assert body[-1]["middleName"] == "Лобной доли"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "865423175266"
    assert body[-1]["birthdate"] == "2024-08-09"
    assert body[-1]["isActive"] is True
    assert body[-1]["id"] == emp_id


def test_get_employees_id():
    # Создать новую компанию
    name = "Булочная"
    descr = "Плюшки, булки, соль"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Обращаемся к компании по ID
    new_company = api.get_company(new_id)
    companyId = new_company['id']

    # получить список сотрудников новой компании
    body = api.get_employees_list(companyId)
    begin_list = len(body)

    # добавить нового сотрудника
    firstName = "Идрак"
    lastName = "Кабзеев"
    middleName = "Малыкал"
    email = "IDRAK@mail.ru"
    url = "string"
    phone = "865837387609"
    birthdate = "2024-08-09"
    new_employee = api.create_employee(firstName, lastName, middleName,
                                       companyId, email, url, phone,
                                       birthdate, isActive=1)
    emp_id = new_employee["id"]
    # получить список сотрудников новой компании
    body = api.get_employees_list(companyId)
    after_list = len(body)
    assert after_list - begin_list == 1

    # Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    assert body[-1]["firstName"] == "Идрак"
    assert body[-1]["lastName"] == "Кабзеев"
    assert body[-1]["middleName"] == "Малыкал"
    assert body[-1]["companyId"] == companyId
    assert body[-1]["phone"] == "865837387609"
    assert body[-1]["birthdate"] == "2024-08-09"
    assert body[-1]["isActive"] is True
    assert body[-1]["id"] == emp_id


def test_patch_employee():
    # Создать новую компанию
    name = "Горный хребет"
    descr = "массажная студия"
    new_company = api.create_company(name, descr)
    new_id = new_company["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)
    companyId = new_company["id"]

    # добавить нового сотрудника
    firstName = "Бу"
    lastName = "ка"
    middleName = "шка"
    email = "slomanhrebet@mail.ru"
    url = "string"
    phone = "86564567877"
    birthdate = "2024-08-09"
    isActive = True
    new_employee = api.create_employee(firstName, lastName, middleName,
                                       companyId, email, url, phone, birthdate,
                                       isActive)
    emp_id = new_employee["id"]

    # получить список сотрудников новой компании
    api.get_employees_list(companyId)

    # Обращаемся к сотруднику по ID
    new_employee = api.get_employee(emp_id)
    employee_id = new_employee["id"]
    # Изменить информацию по сотруднику
    new_lastName = "ма"
    new_email = "mass@mail.ru"
    new_url = "_Updated_"
    new_phone = "Updated"
    new_isActive = False
    edited = api.edit_employee(employee_id, new_lastName, new_email, new_url,
                               new_phone, new_isActive)
    assert edited["email"] == "mass@mail.ru"
    assert edited["url"] == "_Updated_"
    assert edited["isActive"] is False

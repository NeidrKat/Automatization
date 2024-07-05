
from smartphone import Smartphone

catalog = []
# создаем 5 разных телефонов класса Smartphone
phone1 = Smartphone('Samsung', '52A', '+79500000000')
phone2 = Smartphone('Apple', '14pro', '+79520000000')
phone3 = Smartphone('Honor', '90', '+79230000000')
phone4 = Smartphone('Samsung', 'S24', '+79500560000')
phone5 = Smartphone('Huawei', 'PURA', '+79500000023')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f'{phone.marka} - {phone.model}. {phone.number}')

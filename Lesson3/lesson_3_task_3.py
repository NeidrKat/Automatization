from address import Address
from mailing import Mailing

to_address = Address(188691, "г.Кудрово", "ул.Областная", 9, 236)
from_address = Address(427440, "г.Воткинск", "ул.Королева", 27, 28)

sending = Mailing(to_address, from_address, 1500, 56956369)

print(f'Отправление {sending.track} из {sending.f.i}, {sending.f.c},'
      f'{sending.f.str}, {sending.f.h}-{sending.f.f} в {sending.t.i},'
      f'{sending.t.c}, {sending.t.str}, {sending.t.h}-{sending.t.f}'
      f' Стоймость: {sending.c} рублей')

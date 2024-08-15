from address import Address
from mailing import Mailing

address_to=Address(index="123456", city="Москва", street="ул.Сталина", house="15", apartament="33")
address_from=Address(index="654321", city="Таганрог", street="ул.Ленина", house="182", apartament="1")

mailing_out=Mailing(to_address=address_to, from_address=address_from, cost=1000, track="Посылка1228")

print("Отправление",mailing_out.track, "из", mailing_out.from_address.index, mailing_out.from_address.city, mailing_out.from_address.street, 
      mailing_out.from_address.house, "-", mailing_out.from_address.apartament, "в", mailing_out.to_address.index, mailing_out.to_address.city,
      mailing_out.to_address.street, mailing_out.to_address.house, "-", mailing_out.to_address.apartament, ". Стоимость", mailing_out.cost,
      "рублей.")
from mailing import Mailing
from address import Address

send=Mailing(Address(" 123567", "г.Самара", "ул.Ленина", "дом 12 ",  " квартира 67"),
        Address(" 234986",  "г.Ижевск", "ул.Победы", "дом 34 ",  "квартира 32"),
        12000, "1236865")




print(f"Отправление {send.track} из {send.from_address} в {send.to_address}. Стоимость {send.cost} рублей")

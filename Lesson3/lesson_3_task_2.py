from smartphone import Smartphone

catalog=[]

phone1=Smartphone('Apple','14 Pro','+79765346940')

phone2=Smartphone('Xiaomi','K20','+73467129034')

phone3=Smartphone('Samsung','S21','+71297458204')

phone4=Smartphone('Nokia','12','+79045729503')

phone5=Smartphone('OnePlus','X2','+79912034165')

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")

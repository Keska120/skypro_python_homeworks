class Address:
    index='000000'
    city='City_name'
    street='Street_name'
    block='Block_name'
    apartment='Apartment_name'


    def __init__(self,index,city,street,block,apartment):
        self.index=index
        self.city=city
        self.street=street
        self.block=block
        self.apartment=apartment

    def __str__(self):
        return (f"{self.index},{self.city}, {self.street}, {self.block}, {self.apartment}")




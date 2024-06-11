class Address:

    def __init__(self,index,city,street,block,apartment):
        self.index=index
        self.city=city
        self.street=street
        self.block=block
        self.apartment=apartment

    def __str__(self):
        return (f"{self.index},{self.city}, {self.street}, {self.block}, {self.apartment}")




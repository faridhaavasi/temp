class Computer:
    def __init__(self, cpu, ram, hard):
        self.cpu = cpu
        self.ram = ram
        self.hard = hard
    def get_price(self):
        price = self.ram * 10 + self.cpu * 100 + self.hard * 50
        return f'price :  {price} $'      

pc = Computer(3,8,500)
print(pc.get_price())            

class Laptop(Computer):
    def __init__(self, cpu, ram, hard, tuch, size):
        super().__init__(cpu, ram, hard)
        self.tuch = tuch
        self.size = size

    def get_price(self):
        super().get_price()
        price = self.ram * 10 + self.cpu * 100 + self.hard * 50 + self.tuch *100 + self.size * 60
        return f'price :  {price} $'  

pc2 = Laptop(3,8,500,6,17)
print(pc2.get_price())

class Serface(Laptop):
    def __init__(self, cpu, ram, hard, tuch, size,tuch_m):
        super().__init__(cpu, ram, hard, tuch, size)
        self.tuch_m = tuch_m
    def get_price(self):
        super().get_price()
        price = self.ram * 10 + self.cpu * 100 + self.hard * 50 + self.tuch *100 + self.size * 60 + self.tuch_m * 70
        return f'price :  {price} $'
pc3 = Serface(3,8,500,6,17,50)
print(pc3.get_price())    
        
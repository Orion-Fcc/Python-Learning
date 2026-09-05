class Car:
    def __init__(self,brand,name,price):
        self.brand = brand
        self.name = name
        self.price = price
    def running (self):
        print(f'{self.brand} {self.name} 正在高速行驶...')


c1 = Car('BWM','X5',500000)
c2 = Car('BWM','X5',500000)
print(c1)
print(c2)
print(c1==c2)
# print(c1<c2)


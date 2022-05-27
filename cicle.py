class Circle:

    def __init__(self,r:float):
        self.r=r
        self.pi=3.14
    def getArea(self):
        a=self.pi*self.r**2
        return float(a)
    def getPerimeter(self):
        p= 2 * self.pi*self.r
        return p
new_cir=Circle(11)
print(new_cir.getArea())
print(new_cir.getPerimeter())

#link of task : https://backendbaz.ir/practice/4465/
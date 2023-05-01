class Person:
    def __init__(self):
        self.a = 14  #public --> all scop 
        
        self._r = 10 #protected --> class snd class inhariranse

        self.__b = None #privet --> only in class

    def set (self, vlaue):
        '''ster'''
        self.__b = vlaue
    
    def get(self):
        '''geter'''
        return self.__b
    
    def delete(self):
        '''deleter'''
        del self.__b
    b = property(set, get, delete)

p1=Person()
print(p1.a)       
print(p1._r)
print('---------------')

p1._r =2


print(p1.a)       
print(p1._r)
p1.set(1)
print(p1.get())
print(p1.b)

class A:
    VAR = 'A'
    VAR2 = 'A2'
    
    def method(self):
        pass

    
class B:
    VAR = 'B'
    
    def method(self):
        pass

    
class C(B, A):    
    def method(self):
        print(self.VAR, self.VAR2)


class D(C):
    pass


d = D()
d.method()

print(D.__mro__)
# inheritance

# class A:
#     def fun(self,a):
#         self.a=a
#         print(self.a)
# class B(A):
#     def fun1(self,b):
#         self.b=b
#         print(self.b)
# o=B()
# o.fun1("class A")
# o.fun1("class B")   

# polymorphism overloading

# class A:
#     def fun(self):
#         print("class A")
# class B(A):
#     def fun1(self): 
#         print("class B")
# class C(B):
#     def fun2(self):
#         print("class C")        
# o=C()
# o.fun()             

# encapsulation and function overwriting polymorphism

# class A:
#     def fun(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a + self.b)

#     def fun(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a - self.b)

#     def fun(self,a,b):
#         self.a=a
#         self.b=b
#         print(self.a * self.b)
# o=A()
# o.fun(20,2)     

# data abstraction
from abc  import ABC,abstractmethod
class A(ABC):
    def fun(self,a,b):
        self.a = a
        self.b=b
        pass
    @abstractmethod
    def fun1(self):
        print("hello")
class B():
    def fun2(self):
        print("hello class B")
o=B()
o.fun2()                



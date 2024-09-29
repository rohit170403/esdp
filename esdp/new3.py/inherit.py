class A:
    def showA(swlf):
        print("class A")
class B(A):
    def showB(swlf):
        print("class B")
class C(A):
    def showC(self):
        print("Class c")

obj1=A()
obj1.showA()
obj2=B()
obj2.showA()
obj2.showB()
obj3=C()
obj3.showA()
obj3.showC()
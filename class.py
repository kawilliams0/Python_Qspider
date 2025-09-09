class parent():
    def __init__(self):
        print("Hello Williams")
    def add(self,a,b):
        return a+b
class child(parent):
    def __init__(self):
        print("Hello Karthik")
        super().__init__()
    def add(self,a,b):
        return a-b
        
        
obj=child()
print(obj.add(1,2))
print(parent.mro().count())



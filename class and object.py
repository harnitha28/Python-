class stud:
    def __init__(self,a,b,c):
        self.sno=a
        self.sname=b
        self.sage=c
    def display(self):
        print("student no:",self.sno)
        print("student name:",self.sname)
        print("student age :",self.sage)
x=int(input("Enter roll number:"))
y=input("Enter a name:")
z=input("Enter the department:")
obj=stud(x,y,z)
obj.display()

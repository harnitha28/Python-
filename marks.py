class stud:
    def __init__(self,a,b,c,m1,m2,m3):
         self.sno=a
         self.sname=b
         self.sage=c
         self.mark1=m1
         self.mark2=m2
         self.mark3=m3
    def calculate:
        tot=m1+m2+m3
        avg=tot/3
        print("total marks=",tot)
        print("average=",avg)
        if m1>=40 and m2>=40 and m3>=40:
            self.result="pass"
        else:
            self.result="fail"
     def display(self):
         print("student no:",self.no)
         
x=int(input("enter  roll"))
y=input("            

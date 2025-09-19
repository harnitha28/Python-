class Ebill:
    def __init__(self,a,b,c,d,e):
        self.sregno=a
        self.sname=b
        self.scurrent_unit=c
        self.sprevious_unit=d
        self.sper_unit=e
     def calculate(self):
         self.rate=self.scurrent=self.sprevious
         self.amt=self.rate*sel.per_unit
         print("rate=",self.rate)
         print("amount=",self.amt)

      def display(self):
          print("

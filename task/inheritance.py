class customer:
    def __init__(self,name,age):
        self.personname=name
        self.personage=age
    def printname(self):
        print(self.personname,self.personage)

class purchase(customer):
    pass
y=purchase("anila","28 years old")     
y.printname ()  
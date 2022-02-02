class bank():
    def __init__(self,acnt,name,typ,amt):
        self.ac=acnt
        self.nam=name
        self.type=typ
        self.amount=amt
    def printamt(self):
        print("acnt name=",self.nam)
        print("acntnum=",self.ac)
        print("acnt type=",self.type)
        print("bal=",self.amount)
    def withl(self,wl):
     return(self.amount-wl)
n=input("Enter name:")
t=input("Enter type:")
a=int(input("Enter number:"))
am=int(input("Enter amount:"))
obj=bank(a,n,t,am)
print("Account Details")
obj.printamt()
w=int(input("Enter amount to withdraw:"))
print("bl=",obj.withl(w))
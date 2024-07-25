class employee:
    def __init__(self,name,id) :
        self.name = name 
        self.id = id

    def showDetails (self):
        print(f"the name of employee:,{self.id} is {self.name}")

class programmer(employee):
    def showDetails(self):
        print("the default language is python")





e1 = employee("shree", 400)
e1.showDetails()
e2 = programmer("harry ", 4200)
e2.showDetails()
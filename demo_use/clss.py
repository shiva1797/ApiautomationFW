class INFO:
    place='BANG'
    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.clg="new"
    def display(self):
        print(f"name is {self.name} id is {self.id}")


obj1=INFO("SUCHI",111)
obj1.id=112
obj1.display()






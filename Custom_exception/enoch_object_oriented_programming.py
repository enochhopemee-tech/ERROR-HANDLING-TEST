class Student:
    def __init__(self,name,age):
     self.name=name
     self.age=age
    def greet(self):
       print(f"Hello my name is{self.name},Iam{self.age}yrs")
Boy1=Student("Enoch",16)  
Boy2=Student("Great",23)  
(Boy1.greet())   
(Boy2.greet())
       

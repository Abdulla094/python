class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        print("I am a contructor")

    def display(self):
        print("I am a method", self.name , self.age)


#object is created here of class Person and it is assigned to Abdullah

Abdullah = Person("Abdullah",20)
Abdullah.display()
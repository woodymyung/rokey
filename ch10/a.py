class Animal: 
    def speak(self):
        return "Animal speaks"

class Dog(Animal): 
    def speak(self): 
        return "Woof!"

bob = Dog()
print(bob.speak())
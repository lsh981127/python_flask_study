print("2017112197 이승훈")
class Animal: #부모클래스
        def __init__(self, name):
            self.name = name
        def move(self):
            print(self.name, " : move")
        def speak(self):
            pass

class Dog(Animal):     #자식클래스 1
    def speak(self):
        print(self.name, ": bark")

class Duck(Animal):     #자식클래스2
    def speak(self):
        print(self.name, ": quack")

dog = Dog("doggy")
print("Dog name :", dog.name)
dog.move()
dog.speak()

duck = Duck("donald")
print("Duck name: ", duck.name)
duck.move()
duck.speak()

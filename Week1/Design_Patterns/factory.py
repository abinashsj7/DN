class Dog:
    def speak(self):
        return "Bark"


class Cat:
    def speak(self):
        return "Meow"


class AnimalFactory:
    @staticmethod
    def get_animal(animal):
        if animal.lower() == "dog":
            return Dog()
        elif animal.lower() == "cat":
            return Cat()
        else:
            return None


animal = AnimalFactory.get_animal("dog")

if animal:
    print(animal.speak())

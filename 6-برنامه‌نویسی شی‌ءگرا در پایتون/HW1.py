#طراحی سیستم مدیریت حیوانات در باغ وحش

class Animal():
    def __init__(self, name , species, age, sound,Zoo_Name):
        self.name=name
        self.species=species
        self.age=age
        self.sound=sound
        self.zoo_name=Zoo_Name

    def make_sound(self):
        return (self.sound)

    def info(self):
        return (f"esme shir ma {self.name} hast va goone an {self.species} va sen an {self.age} hast, seday on {self.sound} hast va dar baghe vahsh {self.zoo_name} zendegi mikone")
    def __str__(self):
        return self.info()
class Bird(Animal):
    def __init__(self, name, species, age, sound, Zoo_Name, wing_span):
        super().__init__(name, species, age, sound, Zoo_Name)
        self.wing_span=wing_span
    def make_sound(self):
        return self.sound


shir=Animal("simba", "gorbesan", 9, "qoresh","eram")

#part1
print("printing part 1 ...")
print(f"esme shir ma {shir.name} hast va goone an {shir.species} va sen an {shir.age} hast va seday on {shir.sound} hast")
print("part 1 finished ...")

#part2
print("printing part 2 ...")
print(shir.make_sound())
print("part 2 finished ...")

#part3
print("printing part 3 ...")
print(shir.info())
print("part 3 finished ...")

#part4
parande=Bird("fandoq", "tooti", 2, "jik jik", "eram", 20)
print("printing part 4 ...")
print(parande.wing_span)
print(parande.make_sound())
print("part 4 finished ...")

#part5
print("printing part 5 ...")
print(shir)
print("part 5 finished ...")

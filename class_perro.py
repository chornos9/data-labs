class Dog:

    def __init__(self, name, breed, age=0, colour="White"):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = 10
        self.colour = colour

    def bark(self):
        print("WOOF WOOF" if self.age > 1 else "woof woof")

    def human_age(self):
        return self.age * 7

    def lil_leg(self):
        print("Patota" if self.weight > 7 else "Patita!")

    def __str__(self):
        return f"""
                ^..^      /
                /_/\_____/      This is {self.name}
                   /\   /\\         {self.name} is {self.age} years old ({self.human_age()} in human years)
                  /  \ /  \\    {self.name} is a very good {self.breed} :)
"""


class HuntingDog(Dog):

    def bark(self):
        print("WOOF WOOF RUN MOTHERFUCKER")

    def hunt(self):
        print("""                             .--~~,__
                :-....,-------`~~'._.'
                 `-,,,  ,_      ;'~U'
                  _,-' ,'`-__; '--.
                 (_/'~~      ''''(;""")



class competition_dog(Dog):

    def __init__(self, name, breed, age, weight, colour, awards, has_jumped):
        super().__init__(name, breed, age, colour)
        self.awards = awards
        self.has_jumped = False
    
    def bark(self):
        print("runnnnn dog runnnnnn")

    def jump(self, meters):
        if meters < 5:
            print("Here is my jump" +  """                             .-.
     (___________________________()6 `-,
     (   ______________________   /''"`
     //\\                      //\\
jgs  "" ""                     "" """"")
            self.has_jumped = True
        else: 
            print("I cant jump that long")
            self.has_jumped = False
        self.has_won()

    def has_won(self):
        if self.has_jumped:
            self.awards += 1
            return ("I have " + str(self.awards) + " awards")



timmy = Dog("Timmy", "Yorkshire", age=1)
petra = HuntingDog("Petra", "Galgo", age=3)
print(petra)

print(timmy)
timmy.bark()

petra.bark()
petra.hunt()

john = competition_dog("John", "Cocker", 3, 7, "Brown", 1, False)
john.jump(1)
john.has_won()





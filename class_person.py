class Person:  # Clase
    scientific_name = "Homo Sapiens"

    def __init__(self, name, height, age=22):
        self.name = name
        self.height = height
        self.age = age

    def greet(self):
        print("Hello! my name is", self.name, "and I'm", self.age)


# Instancias de "Person"
javi = Person("Javier", 172)
gerardo = Person("Gerardo", 189, age=27)

print(Person.scientific_name)
Person.scientific_name = "Homo Sapiens but with iphones"
print(javi.scientific_name)
print(gerardo.scientific_name)

gerardo.greet()
Person.greet(gerardo)

javi.greet()
javi.age = 123
javi.greet()
javi.name = "Cool Javi"
javi.greet()
gerardo.greet()

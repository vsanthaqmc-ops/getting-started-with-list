class Pet:
    def __init__(self, name, species, age):
       
        self.name = name
        self.species = species
        self.age = age

    def display_profile(self):
        print(f"--- Pet Profile ---")
        print(f"Name: {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age} years old")


my_pet = Pet("Buddy", "Dog", 3)


my_pet.display_profile()
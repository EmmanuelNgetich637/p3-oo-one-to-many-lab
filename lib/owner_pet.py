class Pet:
    def __init__(self, name, pet_type, owner):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        #returns all Pet instances whose owner is this instance
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet only accepts an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        #returns the owner's pets sorted by name
        return sorted(self.pets(), key=lambda pet: pet.name)
    
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]#class variable that lists allowed pet types
    all = []#class variable to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:#validates the pet_type. If invalid, it raises an Exception
            raise Exception(f"Invalid pet_type '{pet_type}. Must be one of {Pet.PET_TYPES}")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):#validates the owner only if it's provided
            raise Exception("Owner must be an instance of Owner or None")
        self.owner = owner

        #keep track of pets
        Pet.all.append(self)


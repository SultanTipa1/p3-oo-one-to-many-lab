class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # Store pets in a private list

    def pets(self):
        return self._pets

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("You can only add a Pet instance.")
        pet.owner = self  # Assign this owner to the pet
        self._pets.append(pet)

    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all pet instances

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type.")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner is not None:
            owner.add_pet(self)  # Automatically add the pet to the owner's list


        Pet.all.append(self)  # Store this pet in the all list


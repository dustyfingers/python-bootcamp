class Pet:
    allowed = ['cat', 'dog', 'fish', 'hamster']

    def __init__(self, name, species):
        if species not in Pet.allowed:
            raise ValueError(f"You can't have a {species} pet!!")
        self.name = name
        self.species = species


nut_nut = Pet("Peanut", "dog")
keke = Pet("Keeva", "dog")

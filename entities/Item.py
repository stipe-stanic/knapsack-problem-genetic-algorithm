class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value

    def __str__(self):
        return repr("Name: " + self.name + "\n" \
                    "Weight: " + str(self.weight) + "\n" \
                    "Value: " + str(self.value) + "\n")

    def __hash__(self):
        return hash(str(self.name))
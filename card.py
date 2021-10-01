class Card:
    def __init__(self, kind, value):
        self.kind = kind
        self.value = value

    def display(self):
        print(f"Card {self.value} of {self.kind}")

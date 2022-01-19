import functools

@functools.total_ordering

class House:
    size = 0
    rooms = 0
    price_qm = 0

    def __init__(self, size=0, rooms=0, price_qm=0):
        self.size = size
        self.rooms = rooms
        self.price_qm = price_qm
    
    def calcPrice(self):
        return self.price_qm*self.size

    def setPrice(self, price):
        self.price_qm = price/self.size

    def getDescription(self):
        return f"Das Haus hat {self.rooms} Räume, {self.size}m² und kostet {self.calcPrice()}€"

    def __str__(self):
        return self.getDescription()
    
    def __lt__(self,other):
        return self.calcPrice() < other.calcPrice()
    
    def __eq__(self,other):
        return self.calcPrice() == other.calcPrice()


h1 = House(100, 5, 20)
h2 = House(60, 3, 30)

print(h1.getDescription())
print(h2.getDescription())

print()

print(f"Haus h1 < h2: {h1 < h2}")
print(f"Haus h1 == h2: {h1 == h2}")
print(f"Haus h1 > h2: {h1 > h2}")
print(f"Haus h1 != h2: {h1 != h2}")
class add():
    def __init__(self, Num1, Num2):
        self.Item1 = Num1
        self.Item2 = Num2

    def __add__(self, other):
        Item1 = self.Item1 + other.Item1
        Item2 = self.Item2 + other.Item2
        Total = (Item1, Item2)
        return Total

    def __str__(self):
        return f"Total ItemsA {self.Item1}  Total ItemsB {self.Item2}"


a = add(6, 10)
b = add(3, 15)
c = a + b
print(c)
print(a.__str__())
print(b.__str__())


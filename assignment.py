class Mother:

   def __init__(self):
       self.height='5.2 ft'
       self.language = 'urdu'

class Father:
    def  __init__(self):
        self.eyecolour = 'brown'
        self.haircolour = 'black'


class Child(Mother,Father):
    def __init__(self):
        Mother.__init__(self)
        Father.__init__(self)
        self.education="B.E"
        self.hair_colour='brown'


c=Child()
print([i for i in dir(c) if "__" not in i])



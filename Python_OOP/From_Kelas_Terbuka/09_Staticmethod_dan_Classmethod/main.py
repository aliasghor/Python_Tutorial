class Hero:
    # Making a private class variabel.
    __total = 0

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

        # Increment everytime when an object is instancied.
        Hero.__total += 1

    # Making a string representation of an object method (it is mainly aimmed the readability for the programmer).
    def __repr__(self):
        return f"{type(self).__name__}('{self.name}')"

    # Retrieve the private class variabel using @classmethod decorator.
    @classmethod
    def totalHero(cls):
        return cls.__total
    
    @staticmethod
    def checkHealth(health: int):
        if health < 0:
            raise ValueError("Error you cannot initalize the health value below than 0!")
        


gerry = Hero("Gerry",100)
mogi = Hero("Mogi",100)

print(gerry)
print(mogi)

print(f"Total instance that has been instancied = {Hero.totalHero()}")
Hero.checkHealth(-1)

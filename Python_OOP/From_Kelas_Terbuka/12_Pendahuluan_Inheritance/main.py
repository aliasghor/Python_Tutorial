"""
    Inheritance is a concept in Object-Oriented Programming (OOP) in which a based class inherits/derives attributes, methods to the derived class; without need to implement or rewrite it all over again from the begining.
"""

class Hero:
    def __init__(self, name: str, health: int, armor: int) -> None:
        self.name = name
        self.health = health
        self.armor = armor

    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.health}, {self.armor})"

class HeroStrength(Hero):
    pass

class HeroIntelligent(Hero):
    pass

gerry = HeroStrength("Gerry",100,40)
mogi = HeroIntelligent("Mogi",150,20)

print(gerry)
print(mogi)

print(help(gerry))
print(help(mogi))
"""
    A super() function is used to retrieve a method that is belong to the super class (based class/parent class).
"""

# An examples the usage of super() function:

class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __str__(self):
        return f"Hero's name: {self.name}; \nHero's health: {self.health}."
    
class HeroStrength(Hero):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)

class HeroIntelligent(Hero):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, health)
    
gerry = HeroIntelligent("Gerry",100)
mogi = HeroStrength("Mogi",50)
print(gerry)
print(mogi)
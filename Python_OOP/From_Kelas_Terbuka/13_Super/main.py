"""
    super() function is used to give access to methods, attributes of parent or sibling class. super() function returns an object that represents the parent class.
"""

class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __str__(self) -> str:
        return f"{self.name} has a health for about = {self.health}"
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.health})"

class HeroStrength(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, 100)

class HeroIntelligent(Hero):
    def __init__(self, name: str) -> None:
        super().__init__(name, 200)


gerry = HeroStrength("Gerry")
mogi = HeroIntelligent("Mogi")

print(gerry)
print(mogi)
print(repr(gerry))
print(repr(mogi))
# Overiding a method from a super class (base class/parent class).

class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __repr__(self):
        return f"Hero('{self.name}', {self.health})"
    
class HeroIntelligent(Hero):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, 100)

    # Overriden a magic method from the derived HeroIntelligent class.
    def __repr__(self):
        return f"HeroIntelligent('{self.name}', {self.health})"
    
class HeroStrength(Hero):
    def __init__(self, name: str, health: int) -> None:
        super().__init__(name, 200)

    # Overriden a magic method from the derived HeroStrength class.
    def __repr__(self):
        return f"HeroStrength('{self.name}', {self.health})"
    

balu = HeroIntelligent("Balu",100)
gerry = HeroStrength("Balu",200)
print(balu)
print(gerry)
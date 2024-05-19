class Hero:
    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health

    def __str__(self):
        return f"Hero's name: {self.name}; has a health for about: {self.health}."

class HeroIntelligent(Hero):
    pass

class HeroStrength(Hero):
    pass

gerry = Hero("Gerry",100)
mogi = HeroIntelligent("Mogi",50)
sampi = HeroStrength("Sampi",30)
print(gerry)
print(mogi)
print(sampi)

print(help(mogi))

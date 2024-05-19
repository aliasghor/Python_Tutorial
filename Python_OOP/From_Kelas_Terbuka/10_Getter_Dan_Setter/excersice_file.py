# @property method is used to give a spesific functionallity to certain methods, making them act as getters, setters, or deleters.

# An example usage of @property method
class Hero:
    def __init__(self, name: str, health: int, armor: int) -> None:
        if not isinstance(name,str):
            raise TypeError(f"Error! expected the first argument attribute value to be a str. Got {type(name).__name__}.")
        self.__name = name

        if not isinstance(health,int):
            raise TypeError(f"Error! expected the second argument attribute value to be an int. Got {type(name).__name__}.")
        self.__health = health

        if not isinstance(armor,int):
            raise TypeError(f"Error! expected the third argument attribute value to be an int. Got {type(name).__name__}.")
        self.__armor = armor

    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def health(self) -> int:
        return self.__health
    
    @health.setter
    def health(self, new_health: int) -> None:
        if not isinstance(new_health,int):
            raise TypeError(f"Error! expected the attribute value to be an int. Got {type(new_health).__name__}.")
        self.__health = new_health

    @health.deleter
    def health(self):
        del self.__health

    @property
    def armor(self) -> int:
        return self.__armor
    
    def __str__(self) -> str:
        return f"{self.name} has health for about = {self.health}. And has an armor for about = {self.armor}."
    
    def __repr__(self) -> str:
        return f"{type(self).__name__}('{self.name}', {self.health}, {self.armor})"
    

gerry = Hero("Gerry",100,40)

print(gerry)
print(repr(gerry))

gerry.health = 40

print(f"Gerry's health after being changed = {gerry.health}")
print(repr(gerry))

del gerry.health
print(gerry.__dict__)


    


    



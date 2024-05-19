class Hero:
    __jumlah = 0

    def __init__(self, name, health, attPower, armor):
        self.__name = name
        self.__healthStandar = health
        self.__attPowerStandar = attPower
        self.__armorStandar = armor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__attPower = self.__attPowerStandar * self.__level
        self.__armor = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Hero.__jumlah += 1

    @property
    def gainExp(self):
        pass
    
    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if self.__exp >= 100:
            print(f"{self.__name} leveled up!")
            self.__level += 1
            self.__exp -= 100
            self.__healthMax = self.__healthStandar * self.__level
            self.__attPower = self.__attPowerStandar * self.__level
            self.__armor = self.__armorStandar * self.__level

    def attack(self, enemy):
        self.gainExp = 50

    # Create a magic method of string representation that is designed to give claritines of the objects (it is mainly designed/aimmed to the users).
    def __str__(self):
        return f"name: {self.__name}; \nlevel: {self.__level}; \nhealth: {self.__health}/{self.__healthMax}; \nattack: {self.__attPower}; \narmor: {self.__armor}."
    
    # Create a magic method of string representation that is not desigend to give claritines of the objects (it is mainly designed/aimmed to the programmers).
    def __repr__(self):
        return f"Hero('{self.__name}', {self.__healthMax}, {self.__attPower}, {self.__armor})"


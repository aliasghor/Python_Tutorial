class Planet:
    def __init__(self, planetName, naturalSatellites):
        self.__planetName = planetName
        self.__naturalSatellites = naturalSatellites

    def getPlanetName(self):
        return self.__planetName
    
    def getNaturalSatellites(self):
        return self.__naturalSatellites 
    
    def __str__(self):
        return f"{self.__planetName} has a natural satellite called {self.__naturalSatellites}"
    

earth = Planet("Earth","Moon")

# Mengambil attributs private melalui methods
data = f"""Nama planet: {earth.getPlanetName()}
Nama satellite: {earth.getNaturalSatellites()}
"""
print(data)

# Mengatur lebar

data = f"""
Nama planet: {earth.getPlanetName(): ^17}
Nama satellite: {earth.getNaturalSatellites(): ^10}
"""
print(data)


print(earth)


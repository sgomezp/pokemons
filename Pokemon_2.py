"""Desarrollo del nuevo juego de Pokemons ;-)"""

from tabulate import tabulate
import random

# Clase principal (parent)
class Pokemon:
    # Constructor
    def __init__(self, name, pk_type, life_points):
        self.name = name
        self.pk_type = pk_type
        self.life_points = life_points
        self.attacks = {"Arañazo": 10}

    def add_attack(self, name_attack, power_attack):
        self.attacks[name_attack] = power_attack


    def attack(self,target):
        if self.attacks:
            random_attack = random.choice(list(self.attacks.keys()))
            print(f"{self.name} usa {random_attack} contra {target.name}")
            power_attack = self.attacks[random_attack]
        else:
            print(f"{self.name} no conoce el ataque {random_attack} ")

    def defenderte(self):
        # Implementación de la defensa
        pass

    def get_weakness(self):
        return self.weakeness


    def get_strength(self):
        return self.strength




# Child classes
class Agua(Pokemon):
    def __init__(self, name, life_points):
        super().__init__(name, "Agua", life_points)
        self.attacks = {"Pistola de agua": 15}
        self.weakeness = ["Planta"]
        self.strength = ["Fuego"]


class Fuego(Pokemon):
    def __init__(self, name, life_points):
        super().__init__(name, "Fuego", life_points)
        self.attacks = {"Lanzallamas": 20}
        self.weakeness = ["Agua"]
        self.strength = ["Planta"]


class Planta(Pokemon):
    def __init__(self,name, life_points):
        super().__init__(name, "Planta", life_points)
        self.attacks = {"Látigo cepa": 30}
        self.weakeness = ["Fuego"]
        self.strength = ["Agua"]


def crea_tabla():
    datos = [
        ["Squirtle", "Charmander", "Bulbasaur"],
        ["Totodile", "Cyndaquil", "Chikorita"],
        ["Mudkip", "Torchic", "Treecko"]
    ]
    # Encabezado de las columnas
    encabezado = ["Agua", "Fuego", "Planta"]

    # Genero tabla
    tabla = tabulate(datos, headers = encabezado, tablefmt="fancy_grid")

    # Imprimir tabla
    print(tabla)


# Crear instancias de la clase Pokemon Agua
squirtle = Agua("Squirtle", 20)
totodile = Agua("Totodile", 20)

# Crear instancias de la clase Planta (Pokémon tipo planta)
bulbasaur = Planta("Bulbasaur", 20)
chikorita = Planta("Chikorita", 40)

# Crear instancias de la clase Fuego
torchic = Fuego("Torchic", 35)
cyndaquil = Fuego("Cyndaquil", 40)

crea_tabla()

squirtle.add_attack("Burbuja", 25)
totodile.add_attack("Burbuja", 25)



print(squirtle.name, squirtle.attacks, squirtle.life_points, squirtle.pk_type, squirtle.weakeness, squirtle.strength)
print(totodile.name, totodile.attacks, totodile.life_points, totodile.pk_type, totodile.weakeness, totodile.strength)
squirtle.attack(bulbasaur)
bulbasaur.attack(chikorita)

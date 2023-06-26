"""Desarrollo del nuevo juego de Pokemo ;-)"""

from tabulate import tabulate

# Clase principal (parent)
class Pokemon:
    # Constructor
    def __init__(self, name, life_points, attacks, weakness, strength):
        self.name = name
        self.life_points = life_points
        self.attacks = {"Arañazo": 10}
        self.strength = [strength]


    def defenderte(self):
        # Implementación de la defensa
        pass

    def get_weakness(self):
        return self.weakeness


    def get_strength(self):
        return self.strength



# Child classes
class Agua(Pokemon):
    def __init__(self, name, life_points, attacks, weakness, strength):
        super().__init__(name, life_points, attacks, weakness, strength)
        self.attacks = {"Pistola de agua": 15} | self.attacks
        self.weakeness = ["Planta"]
        self.strength = ["Fuego"]



class Fuego(Pokemon):
    def __init__(self, name, life_points, attacks, weakness, strength):
        super().__init__(name, life_points, attacks, weakness, strength)
        self.attacks = {"Lanzallamas": 20} | self.attacks
        self.weakeness = ["Agua"]
        self.strength = ["Planta"]



class Planta(Pokemon):
    def __init__(self,name, life_points, attacks, weakness, strength ):
        super().__init__(name, life_points, attacks, weakness, strength)
        self.attacks = {"Látigo cepa": 30} | self.attacks
        self.weakeness = ["Fuego"]
        self.strength = ["Agua"]



def atacar(atacante, attacks, atacado):
    # Implementación del ataque)
    if (type(atacante).__name__ == 'Agua'):
        print(f" {atacante.name} es de agua")
        print(attacks)

    else:
        print("no es de agua")
    pass


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


def escoge_pokemon_atacante():

   atacante = input("escoge el pokemon atacante: ").lower()

   match atacante:
       case totodile.name:
           print("atacante = Tododile")
           return totodile
       case squirtle.name:
           print("atacante = Squirtle")
           return squirtle


# Crear una instancia de la clase Pokemon Agua
squirtle = Agua("Squirtle", 20, {}, [], [])

# creo otro de Agua
totodile = Agua("Totodile", 20, {}, [], [])

# Crear una instancia de la clase Planta (Pokémon tipo planta)
bulbasaur = Planta("Bulbasaur", 20, {}, [], [])

# creo otro de planta
chikorita = Planta("Chikorita", 40, {}, [], [])

crea_tabla()
atacante = (escoge_pokemon_atacante())
print(atacante)
atacar(atacante, atacante.attacks["Pistola de agua"], bulbasaur)



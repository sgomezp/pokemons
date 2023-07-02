"""Desarrollo del nuevo juego de Pokemons ;-)"""
from tabulate import tabulate
import random

#Crear dictionary para guardar los life_points de todos los pokemos: sirve para poder resetear
life_points_dic = {}

# Clase principal (parent)
class Pokemon:
    # Constructor
    def __init__(self, name, pk_type, life_points):
        self.name = name
        self.pk_type = pk_type
        self.life_points = life_points
        self.attacks = {"Arañazo": 10}
        life_points_dic[self.name] = self.life_points

    def defenderte(self):
        # Implementación de la defensa
        pass

    def get_weakness(self):
        return self.weakeness

    def get_strength(self):
        return self.strength

    def add_attack(self, name_attack, power_attack):
        self.attacks[name_attack] = power_attack

    def cal_points(self, target, power_attack):
        if target.pk_type in self.get_weakness():
            lp_temp = target.life_points - (power_attack * 0.5)
        else:
            lp_temp = target.life_points - (power_attack * 2)
        return lp_temp

    def attack(self, target):
        """
        Método que simula un ataque entre el pokemon que lo invoca y un adversario que se pasa como parámetro.
        El ataque se selecciona aleatoriamente entre los disponibles del pokemon invocante.
        Si el pokemon target pierde se resetea el valor de sus life_points
        :param target:
        :return:
        """
        flag = True
        while flag:
            if self.attacks:
                random_attack = random.choice(list(self.attacks.keys()))
                print(f"{self.name} usa {random_attack} contra {target.name}")
                power_attack = self.attacks[random_attack]
                result = self.cal_points(target, power_attack)
                lp_temp = target.life_points
                if result <= 0:
                    print(f"{self.name} le ganó a {target.name}")
                    flag = False
                    target.life_points = life_points_dic[target.name]
                else:
                    print(f"{target.name} ha sobrevivido al ataque de {self.name} quedando sus Life Points en: {result}")
                    lp_temp = target.life_points
                    target.life_points = result


# Child classes
class Agua(Pokemon):
    def __init__(self, name, life_points):
        super().__init__(name, "Agua", life_points)
        super().add_attack("Pistola de agua", 15)
        self.weakeness = ["Planta"]
        self.strength = ["Fuego"]

class Fuego(Pokemon):
    def __init__(self, name, life_points):
        super().__init__(name, "Fuego", life_points)
        super().add_attack("Lanzallamas", 20)
        #self.attacks = {"Lanzallamas": 20}
        self.weakeness = ["Agua"]
        self.strength = ["Planta"]


class Planta(Pokemon):
    def __init__(self,name, life_points):
        super().__init__(name, "Planta", life_points)
        super().add_attack("Látigo cepa", 30)
        #self.attacks = {"Látigo cepa": 30}
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

for key, value in life_points_dic.items():
    print(key, value)

print(squirtle.name, squirtle.attacks, squirtle.life_points, squirtle.pk_type, squirtle.weakeness, squirtle.strength)
print(totodile.name, totodile.attacks, totodile.life_points, totodile.pk_type, totodile.weakeness, totodile.strength)
squirtle.attack(bulbasaur)




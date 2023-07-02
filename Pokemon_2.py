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
        # En un futuro, implementación de la defensa
        pass

    def get_weakness(self):
        return self.weakeness

    def get_strength(self):
        return self.strength

    def add_attack(self, name_attack, power_attack):
        """
        Permite añadir para cada instancia de pokemon nuevos ataques.
        De esta forma puedo agregar ataques únicos a pokemons específicos del mismo tipo
        :param name_attack:
        :param power_attack:
        :return:
        """
        self.attacks[name_attack] = power_attack

    def cal_points(self, target, power_attack):
        """
        Calcula el resultado del combate entre dos pokemons
        :param target:
        :param power_attack:
        :return:
        """
        if target.pk_type in self.get_weakness():
            lp_temp = target.life_points - (power_attack * 0.5)
        else:
            lp_temp = target.life_points - (power_attack * 2)
        return lp_temp

    def attack(self, target):
        """
        Método que simula un ataque entre el pokemon que lo invoca y un adversario que se pasa como parámetro.
        El ataque se selecciona aleatoriamente entre los disponibles del pokemon invocante.
        Cuando el pokemon target pierde se resetea el valor de sus life_points
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
                    print(f"{target.name} ha sobrevivido al ataque de {self.name} quedando sus Life Points en: {result} \n")
                    lp_temp = target.life_points
                    target.life_points = result


# Child classes
class Agua(Pokemon):
    def __init__(self, name, life_points):
        super().__init__(name, "Agua", life_points)
        super().add_attack("Pistola de agua", 40)
        self.weakeness = ["Planta"]
        self.strength = ["Fuego"]

class Fuego(Pokemon):
    def __init__(self, name, life_points):
        super().__init__(name, "Fuego", life_points)
        super().add_attack("Lanzallamas", 90)
        self.weakeness = ["Agua"]
        self.strength = ["Planta"]


class Planta(Pokemon):
    def __init__(self,name, life_points):
        super().__init__(name, "Planta", life_points)
        super().add_attack("Látigo cepa", 45)
        self.weakeness = ["Fuego"]
        self.strength = ["Agua"]

def arma_combate():
    """
    Función que permite pedir al usuario los pokemons que van a combatir
    :return:
    """
    flag = True
    # Solicitar al usuario los nombres de los Pokémon retador y objetivo
    while flag:
        nombre_retador = input("Introduce el nombre del Pokémon retador: ").lower()
        nombre_objetivo = input("Introduce el nombre del Pokémon objetivo: ").lower()
        print()
        # Verificar si los nombres ingresados corresponden a instancias válidas de las clases de Pokémon
        if nombre_retador in globals() and nombre_objetivo in globals():
            retador = globals()[nombre_retador]
            objetivo = globals()[nombre_objetivo]
            # Llamar al método attack() del Pokémon retador pasando el Pokémon objetivo como argumento
            retador.attack(objetivo)
            print()
            seguir = input("Desea otro combate: s/n: ").lower()
        else:
            print("Los nombres de los Pokémon no son válidos.")
        if seguir != "s":
            flag = False
        else:
            flag = True


def crea_tabla():
    """
    Crea una tabla con los pokemons iniciales organizados por su tipo.
    A futuro hay que rediseñar la lógica para incluir nuevos pokemons
    :return:
    """
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
squirtle = Agua("Squirtle", 44)
totodile = Agua("Totodile", 50)
mudkip = Agua("Mudkip", 50)

# Crear instancias de la clase Planta (Pokémon tipo planta)
bulbasaur = Planta("Bulbasaur", 45)
chikorita = Planta("Chikorita", 45)
treecko = Planta("Treecko", 40)

# Crear instancias de la clase Fuego
torchic = Fuego("Torchic", 45)
cyndaquil = Fuego("Cyndaquil", 39)
charmander = Fuego("Chamander",39)

# Añado ataque Burbuja a Squirtle y a Totodile
squirtle.add_attack("Burbuja", 40)
totodile.add_attack("Burbuja", 40)

# Añado ataque Llama Azul a Cyndaquil y Lluvia ígena a Charmander
cyndaquil.add_attack("Llama azul",130)
charmander.add_attack("Lluvia ígnea", 100)

# Añado ataque Bomba germen a Treecko y Hoja aguda a Chikorita
treecko.add_attack("Bomba germen", 55)
chikorita.add_attack("Hoja aguda", 70)

crea_tabla()

arma_combate()





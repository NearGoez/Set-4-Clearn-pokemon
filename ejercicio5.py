import combate_pokemon as pc
from combate_pokemon import quien_parte as qp
from combate_pokemon import calcular_dmg as dmg 
from combate_pokemon import obtener_tipo_pokemon as tipo 

class Pokemon: #definimos el "objeto" pokemon, con las caracteristicas en el orden correspondiente a los inputs(para no escribir dos veces los inputs de caracteristicas pokemon)
    def __init__(self, name, hp, atk, df):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
p1, p2 = Pokemon(input(), int(input()), int(input()), int(input())), Pokemon(input(), int(input()), int(input()), int(input())) #lol
f = [p1 , p2]# los ingresamos en una lista 'f'(de fighters xd), para luego definir un while loop en torno a esta lista y emular los turnos

if qp(p1.name , p2.name) == f[0].name: #verificamos si el pokemon que debe partir esta en la posicion conveniente de la lista, si no, revertimos el orden. (posicion 1)
    f = f[::-1]
print(f'Comienza el combate entre {p1.name} de tipo {tipo(p1.name)} y {p2.name} de tipo {tipo(p2.name)}')

while min(p1.hp, p2.hp)>0: #mientras los dos pokemones tengan puntos de hp, el loop se ejecutara.
    da = dmg(f[1].atk, tipo(f[1].name), f[0].df, tipo(f[0].name)) #hacemos al pokemon en la posicion 1(pokemon que debe partir), atacar al pokemon en la posicion 0 
    print(f'{f[1].name} ha atacado a {f[0].name} provocando {min(da, f[0].hp)} puntos de damage')
    f[0].hp -= da
    f = f[::-1]#revertimos la lista, porque la siguiente iteracion el pokemon 0 debera atacar al pokemon 1.
#la gracia del loop es que utilizamos el hecho de que el pokemon perdedor siempre sera el ultimo pokemon en ser atacado a nuestro favor, es decir, el pokemon en la posicion 1, porque los damos vuelta al final.
print(f'{f[1].name} no puede continuar...')
pc.mostrar_ganador(f[0].name)


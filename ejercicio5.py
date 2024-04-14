import combate_pokemon as pc
from combate_pokemon import quien_parte as qp
from combate_pokemon import calcular_dmg as dmg 
from combate_pokemon import obtener_tipo_pokemon as tipo 

class Pokemon:
    def __init__(self, name, hp, atk, df):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.df = df
p1, p2 = Pokemon(input(), int(input()), int(input()), int(input())), Pokemon(input(), int(input()), int(input()), int(input()))
f = [p1 , p2]

if qp(p1.name , p2.name) == f[0].name:
    f = f[::-1]
print(f'Comienza el combate entre {p1.name} de tipo {tipo(p1.name)} y {p2.name} de tipo {tipo(p2.name)}')
while min(p1.hp, p2.hp)>0:
    da = dmg(f[1].atk, tipo(f[1].name), f[0].df, tipo(f[0].name))
    print(f'{f[1].name} ha atacado a {f[0].name} provocando {min(da, f[0].hp)} puntos de damage')
    f[0].hp -= da
    f = f[::-1]
print(f'{f[1].name} no puede continuar...')
pc.mostrar_ganador(f[0].name)


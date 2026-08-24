import os
os.system("cls")


VPS = 3
TC = -15

contador=0
cantidad_soldados_inmaculados = int(input("Ingrese cantidad de soldados inmaculados:\n"))
cantidad_dothrakis= int(input("Ingrese cantidad de soldados dothrakis:\n"))
vidriagon_disponible= int(input("Ingrese cantidad de dagas disponibles:\n"))
temperatura_actual= float(input("Ingrese temperatura actual en Invernalia:\n"))
existen_dragones=input("Daenerys llevo sus dragones? si - no \n")

ejercito_total = cantidad_soldados_inmaculados + cantidad_dothrakis

vidriagon_necesario = ejercito_total * vidriagon_disponible

deficit_armas =  vidriagon_necesario - vidriagon_disponible

if ejercito_total >= 20000 and existen_dragones == "si" and vidriagon_necesario >= vidriagon_necesario:
    contador += 1 
    print("Victoria Absoluta! El Rey de la Noche ha sido derrotado sin problemas.")
elif ejercito_total == 10000 and existen_dragones == "si" and temperatura_actual <= TC and deficit_armas <= 0:
    print(f"Victoria Amarga: Sobrevivimos gracias al fuego de dragón, pero las bajas por el frío y la falta de armas fueron catastríficas. Faltaron {deficit_armas} dagas.")
    
elif ejercito_total < 10000 and  existen_dragones == "si" and temperatura_actual > TC:
    print("Retirada Tactica: No somos suficientes, pero los dragones, nos dieron tiempo para huir hacia el sur.")
else:
    print("Derrota Total: Invernalia ha caído. Comienza la Larga Noche. . .")
    
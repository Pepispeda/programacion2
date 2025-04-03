# ESTE ES EJERCICIO DE TAREA N|3
import random

def lanzar_dado():
    return random.randint(1, 6)

#pedir nombres#
nombre1 = input("Ingrese el nombre del primer jugador: ")
nombre2 = input("Ingrese el nombre del segundo jugador: ")

#simulamos lanzamiento#
resultado1 = lanzar_dado()
resultado2 = lanzar_dado()

#ahora mostramos resultados#
print(f"{nombre1} obtuvo: {resultado1}")
print(f"{nombre2} obtuvo: {resultado2}")

#ahora determinamos el ganador#
dice_ganador = "empate" if resultado1 == resultado2 else (nombre1 if resultado1 > resultado2 else nombre2)
print(f"El ganador es: {dice_ganador}")

#ACLARACION IMPORANTE LINEA 19 NE ADELANTE LA HICE CON CHAT PORQUE NO LO SABIA HACER#



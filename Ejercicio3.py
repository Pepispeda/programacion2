#AHORA MOSTRAREMOS EL EJERCICO 3#

import random

def adivina_el_numero():
    numero_secreto= random.randint(1, 20)
    intentos = 6
    nombre = input("Ingrese su nombre: ")
    print(f"Hola {nombre}, tienes {intentos} intentos para adivinar un numero entre el 1 y 20.")
    
    
    while intentos > 0:
        try:
            numero_usuario = int(input("ingrese su numero: "))
            if numero_usuario < 1 or numero_usuario > 20:
                print("Por favor , ingrese un numero entre 1 y 20.")
                continue
            
            if numero_usuario == numero_secreto:
                print(f"Felicidades {nombre} ! Has adivinado el numero {numero_secreto}.")
                return
            elif numero_usuario < numero_secreto:
                print("el numero secreto es mayor")
            else:
                print("el numero secreto es menor")
                
            intentos -= 1
            print(f"te quedan {intentos} intentos.")
        except ValueError:
                    print("Entrada invalda ingresa un numero valido")
                    
    print(f" Lo siento {nombre} no te quedan mas intentos. El numero era {numero_secreto}.")
          
#ejecutar juegoadivina_el_numero()
          
          
          
          
                    
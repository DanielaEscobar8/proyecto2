# proyecto: proyecto 2
#autor: Daniela Escobar 
#Carnet: 15032204

from random import randint
from time import  sleep
from screen import clear

marcador = 0
a = 0

#saludar al jugador

print("¡Bienvenido! que tan listo eres reordenando palabras??????? ")

#nombre de la persona
nombre = input("Ingresa tu nombre: ")
print("Hola", nombre ," intenta reordenar las palabras segun el nivel que eligas ¡SUERTE! ")

#ingresa tu genero
genero = input ("Ingresa tu genero: ")

# limpiar y esperar
sleep(3)
clear()

#listas de palabras nivel facil
facil = [ 
    "energia",
    "bullying",
    "contaminación",
    "velocidad",
    "ceramica",
    "graficas",
    "caratula",
    "deposito",
    "ortografico",
    "relampago",
    "romantico",
    "hipopotamo",
    "simpatico",
    "tentaculos",
    "rectangulo",
    "parentesis",
    "academico", 
    "geografico",
    "fantastico",
    "nanometro",
    ]  
#listas de palabras nivel medio
medio = [
    "prefijo",
    "sufijo",
    "compuesto",
    "mezcla",
    "molecula",
    "esencia",
    "sarcastico",
    "antibiotico",
    "tarantula",
    "cuadrilatero",
    "higado",
    "america",
    "arsenico",
    "microfono",
    "antiacido",
    "Sudafrica",
    "Apostrofe"
    "piramide",
    "geometrica"
    "matematicas"
    ]
#listas de palabras nivel dificil
dificil = [
"computadora",
"lexico",
"honestidad",
"amor",
"igualdad",
"honestidad",
"electrico",
"maquina",
"trapaceria",
"esparadrapo",
"fotosintetico",
"murcielago",
"burdegano",
"parafrastico",
"desarrollar",
"ronronear",
"tejemaneje",
"sanguijuela",
"sacacorchos",
"anaranjada",
]
r = 1
while r != 0: 
    
 
    #pregunta que nivel
    print("""
    1. facil
    2. medio
    3. dificil
    """)
    preg1 = input("que nivel deseas jugar: ")

    clear()


    #nivel facil
    if preg1 == "1":
        print("Bienvenido al nivel facil")
        x = 1
        while x != 0:
            juego_pc = randint (0, 19)
            tupalabra = facil[juego_pc]
            total_letras = len(tupalabra)
            vidas = 7
            fallos = 0
            letra=[]
            palabrasadivinadas = 0
           
            while vidas > 0: 
                palabrainvertida=sorted(tupalabra)
                print(*letra, sep=" ")
                print(*palabrainvertida, sep=" ")
                palabracompleta = input("introduzca una palabra: ")

                if palabracompleta not in tupalabra: 
                    vidas -= 1
                    print("estas equivocado")
                    print("tu tienes", +vidas, " vidas")
                else:
                    print("la palabra que escribiste esta correcta")
                    palabrasadivinadas += tupalabra.count(palabracompleta)
                    for i in range (total_letras):
                        if tupalabra [i] == palabracompleta: 
                            tupalabra[i] = palabracompleta  
                            

                if palabracompleta == tupalabra:
                    print("¡Ganaste!")
                    print("la palabra correcta es", tupalabra )
                    marcador += 1
                    break
                if vidas == 0: 
                    print("perdiste")
                    print("la palabra correcta era", tupalabra )  
                    a += 1 
            print("llevas contestando correctamente", marcador)
            print("llevas contestando incorrectamente", a )
            sleep(5)
            clear ()

            x += 1
            if x == 21:
                x = 0
    
        

    #nivel medio
    elif preg1 == "2":
        print("Bienvenido al nivel medio")
        x = 1
        while x != 0:
            juego_pc = randint (0, 19)
            tupalabra = medio[juego_pc]
            total_letras = len(tupalabra)
            vidas = 5
            fallos = 0
            letra=[]
            palabrasadivinadas = 0

            while vidas > 0: 
                palabrainvertida=sorted(tupalabra)
                print(*letra, sep=" ")
                print(*palabrainvertida, sep=" ")
                palabracompleta = input("introduzca una palabra: ")

                if palabracompleta not in tupalabra: 
                    vidas -= 1
                    print("estas equivocado")
                    print("tu tienes", +vidas, " vidas")
                else:
                    print("la palabra que escribiste esta correcta")
                    palabrasadivinadas += tupalabra.count(palabracompleta)
                    for i in range (total_letras):
                        if tupalabra [i] == palabracompleta: 
                            tupalabra[i] = palabracompleta

                if palabracompleta == tupalabra:
                    print("¡Ganaste!")
                    print("la palabra correcta es", tupalabra )
                    marcador += 1
                    break
                if vidas == 0: 
                    print("perdiste")
                    print("la palabra correcta era", tupalabra )  
                    a += 1 
            print("llevas contestando correctamente", marcador)
            print("llevas contestando incorrectamente", a )
            sleep(5)
            clear ()

            x += 1
            if x == 21:
                x = 0
        
    #nivel dificil
    elif preg1 == "3":
        print("Bienvenido al nivel dificil")
        x = 1
        while x != 0:
            juego_pc = randint (0, 19)
            tupalabra = dificil[juego_pc]
            total_letras = len(tupalabra)
            vidas = 3
            fallos = 0
            letra=[]
            palabrasadivinadas = 0

            while vidas > 0: 
                palabrainvertida=sorted(tupalabra)
                print(*letra, sep=" ")
                print(*palabrainvertida, sep=" ")
                palabracompleta = input("introduzca una palabra: ")

                if palabracompleta not in tupalabra: 
                    vidas -= 1
                    print("estas equivocado")
                    print("tu tienes", +vidas, " vidas")
                else:
                    print("la palabra que escribiste esta correcta")
                    palabrasadivinadas += tupalabra.count(palabracompleta)
                    for i in range (total_letras):
                        if tupalabra [i] == palabracompleta: 
                            tupalabra[i] = palabracompleta

                if palabracompleta == tupalabra:
                    print("¡Ganaste!")
                    print("la palabra correcta es", tupalabra )
                    marcador += 1
                    break
                if vidas == 0: 
                    print("perdiste")
                    print("la palabra correcta era", tupalabra )  
                    a += 1 

            print("llevas contestando correctamente", marcador)
            print("llevas contestando incorrectamente", a )
            sleep(5)
            clear ()
            x += 1
            if x == 3:
                x = 0

#cuantas respondio bien en el nivel
    print("respondiste correctamente", marcador)
    print("respondiste incorrectamente", a )
    sleep(5)
    clear()
#pregunta si quiere volver a jugar
    respuesta = input("si / no: ")
    if respuesta == "si": 
        r = 1 
    else: 
        r = 0
    sleep(5)
    clear()
    
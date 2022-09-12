import random
import time

coches = ["ford", "audi", "nissan", "renault", "chevrolet", "mitsubishi", "cadillac", "suzuki", "porsche", "lamborghini"]
paises = [ "mexico", "colombia", "canada", "venezuela", "uruguay", "argentina","guatemala", "panama", "ecuador", "alemania"]
colores = ["rojo", "amarillo", "verde", "salmón", "azul", "naranja", "cafe", "negro", "blanco", "morado"]
nombres = ["cristobal", "amaranto", "leonardo", "camilo", "gustavo", "federico", "ruben", "alejandro", "nicolas", "elizabeth"]
print("El ahorcado")
print("El objetivo del juego es adivinar la palabra secreta letra por letra")
print("Tienes 5 vidas, pierdes una vida cada vez que te equivocas de letra y si te quedas sin vidas pierdes")
print("Puedes jugar con palabras que son marcas de coches, nombres de paises, colores o nombres")
time.sleep(5)
print("Vas a tener diferentes categorías con las que puedes jugar.")
print("Cada categoría tiene un código.")
cat_seleccionada = input("Ingresa ""a"" para marcas de coches, ""p"" para nombres de paises, ""c"" para colores o ""n"" para nombres. ")
while True:
    if cat_seleccionada.lower() == "a":
        print("Has seleccionado marcas de coches")
        palabra_secreta = random.choice(coches)
        break
    elif cat_seleccionada.lower() == "p":
        print("Has seleccionado nombres de paises")
        palabra_secreta = random.choice(paises)
        break
    elif cat_seleccionada.lower() == "c":
        print("Has seleccionado colores")
        palabra_secreta = random.choice(colores)
        break
    elif cat_seleccionada.lower() == "n":
        print("Has seleccionado nombres")
        palabra_secreta = random.choice(nombres)
        break
    else:
        print("Por favor selecciona una categoria válida")
        cat_seleccionada = input("Ingresa ""a"" para marcas de coches, ""p"" para nombres de paises, ""c"" para colores o ""n"" para nombres ")

vidas = 5
lista_letras_adivinadas = []

print('_' * len(palabra_secreta))
while True:
    while True:
        letra_adivinada = input("Adivina una letra: ")
        if(len(letra_adivinada)!=1 and letra_adivinada.isnumeric()):
            print("Eso no es una letra intenta con una sola letra")
        else:
            if letra_adivinada.lower() in lista_letras_adivinadas:
                print("Ya habías intentado con esa letra, intenta con otra por favor")
            else:
                lista_letras_adivinadas.append(letra_adivinada)
                if letra_adivinada.lower() in palabra_secreta:
                    print("Adivinaste una letra, buen trabajo.")
                    break
                else:
                    vidas = vidas-1
                    print("Te haz equivocado y perdido una vida")
                    print("Pierdes una vida :(")
                    print("Te quedan " + str(vidas) + " vidas")
                    break
    if vidas==0:
        print("Haz perdido. La palabra secreta era: "+ palabra_secreta)
        break
    estatus_actual = ""
    letras_faltantes = 0
    for letra in palabra_secreta:
        if letra in lista_letras_adivinadas:
            estatus_actual = estatus_actual + letra
        else:
            estatus_actual = estatus_actual + "_"
            letras_faltantes = letras_faltantes + 1

    print(estatus_actual)
    if letras_faltantes == 0:
        print("Ganaste, Felicidades.")
        print("La palabra secreta era: " + palabra_secreta)
        break

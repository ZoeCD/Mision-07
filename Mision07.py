# Zoe Caballero Dominguez A01747247
# Este programa hace dos cosas diferentes utilizando los ciclos while:
#1. Hace una división entre dos números
#2. Encuentra el número mayor de una serie dada por el usuario.


#Esta función encruentra el numero mayor de los numeros dados por el usuario
def encontrarMayor():
    print("Teclea una serie de números para encontrar el mayor.")
    numeroA = int(input("Teclea un número [-1 para salir]: "))
    numeroB = -1
    while numeroA != -1:
        if numeroA > numeroB:
            numeroB = numeroA
        else:
            pass
        numeroA = int(input("Teclea un número [-1 para salir]: "))

    if numeroA == -1 and numeroA >= numeroB:
        print("No hay valor mayor")
    else:
        print("El mayor es:", numeroB)


#Hace una división entre dos números restando el divisor del dividendo.
def dividir(dividendo, divisor):
    cantidad = dividendo
    contador = 0
    while cantidad >= divisor:
        cantidad = cantidad - divisor
        contador += 1
    print ("%d / %d = %d, sobra %d" %(dividendo, divisor, contador, cantidad))


#Imprime el menú de opciones y lee lo que quiere hacer el usuario
def leerOpcionMenu():
    print("Misión 07. Ciclos While")
    print("Autor: Zoe Caballero Dominguez")
    print("Matrícula: A01747247")
    print("1. Calcular divisores")
    print("2. Encontrar el mayor")
    print("3. Salir")
    opcion = int(input("Teclea tu opción: "))
    return opcion


#Función principal
def main():
    opcion = leerOpcionMenu()

    while opcion != 3:
        if opcion == 1:
            print("")
            print("Calculando divisores")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor)
        elif opcion == 2:
            print("")
            encontrarMayor()
        elif opcion<1 or opcion>3:
            print("ERROR, teclea 1, 2 o 3.")

        print("""
""")
        opcion = leerOpcionMenu()
    print("")
    print("Gracias por usar este programa, regresa pronto.")


#Llamar a la función main
main()
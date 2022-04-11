# Crear un programa donde dada una palabra, se busque en una frase y devuelva la
# cantidad de veces que aparece en ella. La frase y la palabra deben ser parámetros
# de una función (La frase puede contener puntos, comas y punto y comas, por tanto
# deberá limpiarla que no los contenga).

# Funcion saludo
def saludo():
    print("\nBienvenid@s, este programa calcula cuantas veces esta una palabra en una frase")
    print("-----------------------------------------------------------------------------------\n")

# Funcion pedir Datos al usuario
def pedir_datos():
    frase = input("Ingrese una frase: ")
    palabra = input("Ingrese la palabra que desea buscar en la frase: ")
    return frase, palabra

# Funcion limpiar signos
def limpiar_datos(frase, palabra):
    frase = list(frase)
    bandera = True
    frase_limpia = ""
    while bandera:
        for letra in frase:
            if letra == "." or letra == "," or letra == ":" or letra == ";":
                posicion = int(frase.index(letra))
                frase.pop(posicion)
        bandera = False
    for letra in frase:
        frase_limpia += letra
    return frase_limpia

# Funcion buscar palabra
def buscar_palabra(frase_limpia, palabra):
    frase_limpia = frase_limpia.split(" ")
    cantidad = frase_limpia.count(palabra)
    print("\nResultado")
    print("---------------------------")
    print(f"El numero de veces que esta la palabra {palabra} en la frase es: {cantidad} ")

# Funcion despedida
def despedida():
    print("\nFin del programa")
    print("---------------------------")

# Funcion principal
def funcion_principal():
    saludo()
    [frase, palabra] = pedir_datos()
    frase_limpia = limpiar_datos(frase, palabra)
    buscar_palabra(frase_limpia, palabra)
    despedida()
funcion_principal()
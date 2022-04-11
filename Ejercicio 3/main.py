# Importando la clase DNI
from dni import Dni

# Saludo
print("\nBienvenid@, este programa determina si el DNI ingresado es valido o no.\n")

# Creando el objeto
dni_ciudadano = input("Ingrese su DNI: ")
tomando_dni = Dni()
validar = tomando_dni.validar_dni(dni_ciudadano)
if validar == True:
    print("El DNI ingresado es valido")
else:
    print("El DNI ingresado es invalido")
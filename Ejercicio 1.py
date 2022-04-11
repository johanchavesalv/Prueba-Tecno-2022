#Crear un programa que con dos puntos cardinales donde pasa una línea recta en el
#plano cartesiano, se obtenga la ecuación lineal que representa la recta 


# Saludo
print("\nBienvenido, este programa calcula la ecuacion de una recta que pasa por dos puntos dados por el usuario.\n")

# Datos pedidos al usuario
print("\nCoordenadas del punto 1, P1(x1, y1)")
print("---------------------------------------")
x_1 = float(input("Ingrese la coordenada x1: "))
y_1 = float(input("Ingrese la coordenada y1: "))

print("\nCoordenadas del punto 2, P2(x2, y2)")
print("---------------------------------------")
x_2 = float(input("Ingrese la coordenada x2: "))
y_2 = float(input("Ingrese la coordenada y2: "))

# Calculo de la pendiente
m = round((y_2 - y_1)/(x_2-x_1), 2)

# Calculo del corte con el eje y, "b", b = y - mx
b = round(y_1 - m*x_1)

# Resultados
print("\nResultados.")
print("-----------------------------------------")
if b < 0:
    print(f"La ecuacion de la recta con los puntos P1({x_1}, {y_1}) y P2({x_2}, {y_2}) es:\ny = {m}x + ({b})")
else:
    print(f"La ecuacion de la recta con los puntos P1({x_1}, {y_1}) y P2({x_2}, {y_2}) es:\ny = {m}x + {b}")

# Despedida
print("\nFin del programa.")
print("---------------------------------------")
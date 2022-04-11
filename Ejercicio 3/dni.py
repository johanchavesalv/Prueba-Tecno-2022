class Dni:
    def __init__(self):
        self.letras = ["T", "R", "W", "A", "G", "M", "Y", "F", "P", "D", "X", "B", "N", "J", "Z", "S", "Q", "V", "H", "L", "C", "K", "E"]

    def validar_dni(self, dni_ciudadano):
        bandera = True
        dimension = len(dni_ciudadano)
        
        for letra in self.letras:
            for posicion in range(0, dimension-1):
                if letra == dni_ciudadano[posicion]:
                    bandera = False

        if  bandera == False:
            return False 
        elif dimension != 9:
            return False
        else:         
            numero  = int(dni_ciudadano[0:dimension-1])
            modulo = numero%23 
            letra_dni = dni_ciudadano[dimension-1] 
            if letra_dni == self.letras[modulo]:
                return True
            else:
                return False
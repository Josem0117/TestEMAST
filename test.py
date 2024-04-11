import math

class Figura:
    pass

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado ** 2

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return 0.5 * self.base * self.altura

def main():
    try:
        opcion = int(input("Ingrese el número de la figura (1: círculo, 2: cuadrado, 3: rectángulo, 4: triángulo): "))

        if opcion == 1:
            radio = float(input("Ingrese el radio del círculo: "))
            figura = Circulo(radio)
        elif opcion == 2:
            lado = float(input("Ingrese el lado del cuadrado: "))
            figura = Cuadrado(lado)
        elif opcion == 3:
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            figura = Rectangulo(base, altura)
        elif opcion == 4:
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            figura = Triangulo(base, altura)
        else:
            print("Opción no válida.")
            return
    except ValueError:
        print("Debe ingresar un numero")
        return
    area = figura.calcular_area()
    print(f"El área de la figura es: {area}")

main()

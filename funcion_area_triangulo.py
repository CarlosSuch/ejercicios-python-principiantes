'''
__________________Calcular el área de un triangulo_______________________

Crea una función que tome la base y la altura de un triangulo y devuelva su área. 

Fórmula:   (base * altura) / 2

- Usa return 

La base sea: 12
La altura sea: 10

'''


# Solución
def area_triangulo(b,a):
    return (b * a) / 2
b = 12
a = 10
print(area_triangulo(b,a))

# 2 Solución
def averiguar_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
base = 12
altura = 10
print(averiguar_area_triangulo(base,altura))

# 3 solución  Lambda
tri_area=lambda b,a:(b*a)/2
print(tri_area(12,10))


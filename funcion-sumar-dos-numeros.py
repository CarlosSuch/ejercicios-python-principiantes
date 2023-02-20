'''
   ____________  DEVUELVE LA SUMA DE DOS NÚMEROS ______________
   
   ¿Qué tienes que hacer?

   1. Crear una función
   2. Tomar dos números como argumentos
   3. Devolver la suma
   4. Usar return en el resultado

ejemplos:
suma(4, 9)      ->  13
suma(-5, -10)   -> -15

'''

# 1 solución
def suma(a, b):
    return a + b
# imprimimos en pantalla
print(suma(4,9))

# 2 solución 
def suma_dos(numero1, numero2):
    sumita = numero1 + numero2
    return sumita
# imprimimos la comprobación por pantalla
print(suma_dos(-5, -10))
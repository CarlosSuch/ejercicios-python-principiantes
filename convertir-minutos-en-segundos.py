'''
__________CONVERTIR MINUTOS EN SEGUNDOS__________

Este ejercicio consiste en crear una función de Python que permita convertir minutos (en números enteros) a segundos. 

La función recibirá una variable llamada 'minutos', la cual será un entero, y devolverá un entero correspondiente a la cantidad de segundos equivalentes. Por ejemplo, si se pasa un argumento de 5 minutos, la función devolverá 300 segundos.

Extra: Usa return 

'''


# 1 solución 
def minutos_segundos(num):
    return num * 60
# Imprimimos la comprobación en pantalla
print(minutos_segundos(5))


# 2 solución
def de_minutos_a_segundos(numero):
    resultado = numero * 60
    return resultado
# Lo mostramos por pantalla
print(de_minutos_a_segundos(25))



'''
______________Devolver el siguiente número_____________

En este ejercicio se pide que se cree una función, que se tomará como argumento, y tenemos que incrementar su valor en 1. 

ejemplos: 

incrementar(2)   -> 3
incrementar(8)   -> 9
incrementar(-2)  -> -1
'''
# Mi solución
def incrementar(numero):
    return numero + 1
# Mostramos por pantalla un resultado, en este caso elegimos el número 89 para que le sume 1. 
print(incrementar(89))

# 2 Solución
def incremento(num):
    num = num + 1
    return num 
# Mostramos por pantalla otro resultado, en este caso con el número 8. 
print(incremento(8))
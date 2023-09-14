def nuemro_cuadrado(numero):
    """
    se ingresa un numero entero menor a 10 y se retorna
    en numero al cuadrado si es menor a 10 sino se devuelve error por falta de memoria
    """
    if numero > 10:
      return(numero*numero)
    else:
       return "Error por falta de memoria"
print (nuemro_cuadrado(-11))




scribir una función que reciba como primer parámetro una temperatura en grados, y como segundo parámetro: 'F' o 'C', para indicar la escala (F = Fahrenheit y C = Celsius).
La función debe devolver el valor equivalente en la escala no indicada como segundo parámetro.
Tener en cuenta que: F = (C * 1,8) + 32.



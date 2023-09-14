def hay_diptongo(palabra):
    """
    Funcion que recibe una palabra y retorna True si la misma
    tiene diptongo, o False, si no lo tiene.
    >>> hay_diptongo("ciudad")
    True
    >>> hay_diptongo("autódromo")
    True
    >>> hay_diptongo("estación")
    True
    >>> hay_diptongo("silla")
    False
    """

    l_diptongo = []
    for letra_1 in ["u", "i"]:
        for letra_2 in ["a", "e", "o", "á", "é", "ó"]:
            l_diptongo.append( letra_1 + letra_2 )
            l_diptongo.append( letra_2 + letra_1)

    l_diptongo.extend(["ui", "iu"])
    # Control de si alguno de los diptongos forma parte de la palabra
    devolver = True
    posicion = 0
    while posicion < len(l_diptongo) and l_diptongo[posicion] not in palabra:
        posicion += 1
        if posicion == len(l_diptongo):
            devolver = False
    return devolver
#----------------------- Bloque Principal ---------------------------#
import doctest
print(doctest.testmod())

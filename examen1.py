""" Paso 1: Crear una lista de valores impares entre 0 y 100
    Paso 2: Eliminar valores divisibles por 9
    Paso 3: Incrementar en 1 los valores múltiplos de 3
    Paso 4: Sumar todos los elementos pares en la lista"""
valores_impares = [x for x in range(1, 101, 2)]

valores_impares = [x for x in valores_impares if x % 9 != 0]

valores_impares = [x + 1 if x % 3 == 0 else x for x in valores_impares]

suma_elementos_pares = sum([x for x in valores_impares if x % 2 == 0])

print("Lista de valores impares después de las operaciones:")
print(valores_impares)
print("Suma de elementos pares en la lista:", suma_elementos_pares)

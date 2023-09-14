def generar_diccionario_stock(datos):
    stock = {}
for producto, accion, cantidad in datos:
    if producto not in stock:
     stock[producto]= 0
     if accion =="C":
         stock[productos]+=cantidad
    elif accion == "V":
        stock [producto] -= cantidad

if __name__ == "__main__":
    datos = [
        (
"arroz", "C", 20),
        (
       
"papa", "C", 40),
        (
       
"arroz", "V", 15),
        (
       
"fideos", "C", 25),
        (
       
"papa", "V", 10),
        (
       
"papa", "V", 10),
        (
       
"arroz", "C", 10),
        (

"fideos", "V", 20),
    ]
    stock_resultado = generar_diccionario_stock(datos)

print(stock_resultado)
















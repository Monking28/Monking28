import csv
abc = ["a", "b", "c", "d", "e", "f", "g","h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc_inv = ["z","y","x","w","v","u","t","s","r","q","p","o","ñ","n","m","l","k","j","i","h","g","f","e","d","c","b","a"]
def cifrar_C(cadena, clave):
    resultado = []
    for caracter in cadena:
        if caracter.isalpha():
            desplazamiento = ord('a') if caracter.islower() else ord('A')
            letra_cifrada = chr(((ord(caracter) - desplazamiento + clave) % 26) + desplazamiento)
        else:
            letra_cifrada = caracter
        resultado.append(letra_cifrada)
    return ''.join(resultado)
  
def  descifrar_C(cadena, clave):
    resultado = []
    for caracter in cadena:
        if caracter.isalpha():
            desplazamiento = ord('a') if caracter.islower() else ord('A')
            letra_descifrada = chr(((ord(caracter) - desplazamiento - clave) % 26) + desplazamiento)
        else:
            letra_descifrada = caracter
        resultado.append(letra_descifrada)
    return ''.join(resultado)
def cifrar_A(cadena):
    cifrado = ""
    for caracter in cadena:
        if caracter in abc:
            cifrado += abc_inv[abc.index(caracter)]
        elif caracter == " ":
            cifrado += caracter
    return cifrado
def descifrar_A(cadena):
    descifrado = ""
    for caracter in cadena:
        if caracter in abc_inv:
            descifrado += abc[abc_inv.index(caracter)]
        elif caracter == " ":
            descifrado += caracter
    return descifrado
  
def validar_destinatario(destinatario): 
  if destinatario == "*":
      return True
  elif len(destinatario) >= 5 and len(destinatario) <= 15:
        caracteres_validos = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-."
        for caracter in destinatario:
            if caracter not in caracteres_validos:
                return False
        return True
  else:
        return False

def consultar_mensajes(destinatario):
    if validar_destinatario(destinatario) == False:
        print("ALERTA: Usted es un intruso")
    else:
        with open("destinatarios.csv", "r") as file:
            csvreader = csv.reader(file)
            next(csvreader)
            mensajes = []
            for row in csvreader:
                if row[0] == destinatario or row[0] == "*":
                    mensajes.append(row[2])
            if len(mensajes) == 0:
                print("No hay mensajes para mostrar")
            else:
                print("Mensajes cifrados:")
                print("------------------")
                for mensaje in mensajes:
                    if destinatario != "*":
                        print(destinatario.upper() + ": " + mensaje)
                    else:
                        print("TODOS: " + mensaje)
                print("------------------")
op = 1
while op != 5:
    print ("Que desea hacer?\n 1) Cifrar Mensaje \n 2) Descifrar mensaje\n 3) Enviar mensaje cifrado\n 4)Consultar mensajes cifrados\n 5)Salir.")
    op = int(input('Ingresa una opcion: '))

    if op == 1:
       cadena = input("Ingrese su mensaje: ")
       pregunta_a_c = input("Que cifrado desea a/c: ")
       if pregunta_a_c == "a":
        print(cifrar_A(cadena))
       elif pregunta_a_c == "c":
           clave = int(input("Ingrese la clave de cifrado: "))
           mensaje_cifrado = cifrar_C(cadena, clave)
           print("Mensaje cifrado:", mensaje_cifrado)
    elif op == 2:
       cadena = input("Ingrese su mensaje: ")
       desifrar_a_c = input("Que cifrado desea descifrar a/c:")
       if desifrar_a_c == "a":
           print(descifrar_A(cadena))
       elif desifrar_a_c == "c":
        clave = int(input("Ingrese la clave de descifrado: "))
        mensaje = descifrar_C(cadena, clave)
        print("Mensaje Descifrado: ", mensaje)
    elif op == 3 :
       cadena = input("Ingrese su mensaje: ")
       pregunta_cifrar = input("Que cifrado desea a/c: ")
       if pregunta_cifrar == "a":
        resul = cifrar_A(cadena)
        codigo = "A"
        destinatario = input("ingrese un destinatario: ")
       elif pregunta_cifrar == "c":
        clave = int(input("Ingrese la clave de cifrado: "))
        mensaje_cifrado = cifrar_C(cadena, clave)
        print("Mensaje cifrado:", mensaje_cifrado)
        resul = cifrar_C(cadena,clave)
        codigo = "C"
        destinatario = input("ingrese un destinatario: ")
        if validar_destinatario(destinatario) == False:
           print("El destinatario ingresado es invaido")
        else:
             miarchivo = open("destinatarios.csv","w")
             csvwriter = csv.writer(miarchivo)
             encabezado = ["Destinatario","Cifrado", "Mensaje"]
             lista_datos = [destinatario,codigo,resul]
             csvwriter.writerow(encabezado)
             csvwriter.writerow(lista_datos)
    elif op == 4 :
           destinatario = input("Ingrese su identificador de usuario: ")
           consultar_mensajes(destinatario)
  
    elif op == 5: 
        print('Saliendo ')

    else:
        print('Ingrese una opcion valida')

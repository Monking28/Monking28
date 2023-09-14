desde  la importación de tkinter  * 
desde  el cuadro de mensajes de importación de tkinter  
def  obtener_usuarios_claves ():
    return { "Andrés" : "AndrésJ" ,
            "Pablo" : "PabloG" ,
            "Gustavo" : "GustavoB" }
def  validar ( usuario , contraseña ):
    credenciales  =  obtener_usuarios_claves ()

    si  usuario  en  credenciales  y  credenciales . obtener ( usuario ) ==  contraseña :
        cuadro de mensaje . showinfo ( mensaje = "Usuario y Clave Correctos" )
    más :
        cuadro de mensaje . showerror ( mensaje = "Algunos de los datos ingresados ​​es Incorrecto" )
def  ventana_login ():
    raiz  =  Tk ()
    raíz . título ( "Iniciar sesión Grupo Cátedra" )
    raíz . redimensionable ( Falso , Falso )

    raíz . geometría ( "300x130" )
    raíz . configuración ( bg  =  "azul" )
    mi_frame  =  Marco ()
    mi_marco . paquete ()
    mi_marco . configuración ( bg  =  "azul" , ancho  =  "300" , alto  =  "130" )
    Etiqueta ( mi_frame , texto  =  "Usuario Alumno: " ). lugar ( x  =  10 , y  =  20 )
    box_alumno  =  Entrada ( mi_frame )
    cuadro_alumno . lugar ( x  =  130 , y  =  20 )
    Etiqueta ( mi_frame , texto  =  "Clave: " ). lugar ( x  =  10 , y  =  50 )
    box_clave  =  Entrada ( mi_frame )
    caja_clave . lugar ( x  =  130 , y  =  50 )
    caja_clave . configuración ( mostrar  =  "*" )
    mi_marco . configuración ( ancho  =  "300" , alto  =  "100" )
    boton_ingresar  =  Botón ( raiz , texto  =  "Ingresar" , \
    comando  =  lambda : validar ( box_alumno . get (), box_clave . get ()))
    botón_ingresar . paquete ()
    raíz . bucle principal

ventana_login ()

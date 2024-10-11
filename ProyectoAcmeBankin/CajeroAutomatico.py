# Creamos nuestros diccionarios separadas para tener un mejor orden en el almacenamiento
# Creamos un menu principal basico que me retorna el valor ingresado por el usuario
from Modulos.funciones import *
from Modulos.diccionarios import *
def menu_principal():
    menu = input('''
--------------------------------------------
-------------MENU PRINCIPAL-----------------
--------------------------------------------
(1). Crear una cuenta bancaria
(2). Consignar dinero a una cuenta
(3). Retirar dinero
(4). Pagar servicios
(5). Mostrar movimientos bancarios
(0). Cerrar programa

Elija una opcion a realizar: ''')
    return menu

# Mi menu principal te notifica si la opcion que elegiste esta fuera del rango establecido
while True:
    opc = menu_principal()
    match opc:
        case '1':
            registro_usuario()
        case '2':
            consignar_dinero()
        case '3':
            retirar_dinero()
        case '4':
            pagar_servicios()
        case '5':
            movimientos_bancarios()
        case '0':
            print('Finalizando programa...')
            break
        case _:
            print('''
        ------LA OPCION NO ESTA DENTRO DEL RANGO-------
        --INGRESE UN VALOR ENTRE (1-5). 0 PARA SALIR.--''')
# Como conclusion
# Me ayudó mucho descubrir el bucle for con doble indice
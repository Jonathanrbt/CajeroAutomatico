# Importamos todos los diccionarios e indices para  iterarlos y verificar si existen
from Modulos.diccionarios import cuentas, movimientos, indice


#Pide el numero de cuenta y su clave si estas coinciden con las registradas retorna True y 
#El numero de cuenta que se ingreso
def ingreso ():
    numcuent = input('''
-------------------------------------------
----------VERIFICACION DE USUARIO----------
-------------------------------------------

Ingrese el numero de cuenta: 

''')
    clave = input('Ingrese la clave de su cuenta: ')
    usuario_encontrado = False
    while not usuario_encontrado:
        for i in cuentas.values():  
            if numcuent == str(i['numCuenta']) and clave == i['clave']:
                usuario_encontrado = True
                return True, numcuent
        if not usuario_encontrado:
                numcuent = input('''
--------------------------------
EL DATO INGRESADO ES INCORRECTO
SELECCIONE NUEVAMENTE UNA OPCION
--------------------------------

Ingrese el numero de cuenta:''')
                clave = input('Ingrese la clave de su cuenta: ')
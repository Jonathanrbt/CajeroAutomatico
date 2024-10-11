# Importo la variable indice, para poderla modificar dentro de la funcion
# Importamos nuestros diccionarios
import datetime 
from Modulos.diccionarios import cuentas, movimientos, indice
from Modulos.login import ingreso
llaveMovimientos = 0
referenciaConsignaciones = 56




# Mi funcion de registro no permite crear cuentas bancarias con cedula de ciudadania existentes
# Por temas de errores en las siguientes funciones que piden las cedulas
def registro_usuario():
    global cuentas
    global indice
    cedula = input('''
-------------------------------------------
-----------CREAR CUENTA BANCARIA-----------
-------------------------------------------

Ingrese la cedula para crear su cuenta: ''')
    # Este bucle dejara de ejecutarse hasta que el usuario ingrese una cedula no existente
    documento_existente = True
    while documento_existente:
        documento_existente = False
        for valor in cuentas.values():
            if cedula == valor['documento']:
                documento_existente = True
                cedula = input('''
------------------------------
CEDULA DE CIUDADANIA EXISTENTE
------------------------------

Por favor ingrese una nueva: ''')
        if not documento_existente:
            cuentas[indice] = {
                'numCuenta': indice,
                'documento': cedula,
                'nombre': input('Ingrese el nombre para crear su cuenta: '), 
                'clave': input('Ingrese la clave para crear su nueva cuenta: '), 
                'saldo': 0,
                'Tiempo': datetime.datetime.today()}
            print(f'''
-------------------------------------------------
SU CUENTA QUEDO REGISTRADA DE LA SIGUIENTE MANERA
-------------------------------------------------

Numero de cuenta: {cuentas[indice]['numCuenta']}
Cedula de ciudadania: {cuentas[indice]['documento']}
Nombre del usuario: {cuentas[indice]['nombre']}
Clave de la cuenta: {cuentas[indice]['clave']}
Saldo: {cuentas[indice]['saldo']}
Su cuenta quedó registrada a las: {cuentas[indice]['Tiempo']}
''')
            # Este indice solo se incrementa cuando se crea una nueva cuenta, ya que el nos lleva el conteo de cuentas creadas
            # Para asignarle un numero de cuenta diferente a cada usuario
            indice += 1





#Pregunta el numero de documento o el numero de cuenta para encontrar una cuenta a la cual consignar dinero
def consignar_dinero():
    global referenciaConsignaciones
    global llaveMovimientos
    ingreso = input('''
-------------------------------------------
-------------CONSIGNAR DINERO--------------
-------------------------------------------

(1). Ingresar con el numero de documento
(2). Ingresar con el numero de cuenta 

''')
    doc = ''
    num = ''
    if ingreso == '1':
        doc = input('Ingrese su documento: ')
    if ingreso == '2':
        num = input('Ingrese su numero de cuenta: ')
    usuario_encontrado = False
    while not usuario_encontrado:
        for llaveCuentas, valor in cuentas.items():
            if num == str(valor['numCuenta']) or doc == valor['documento']:
                usuario_encontrado = True
                cantidad = float(input('Ingrese la cantidad que desea consignar: '))
                # Este while nos permite controlar que el usuario no ingrese valores negativos o en cero
                # Por que le podria restar el saldo al usuario
                while cantidad <= 0:
                        cantidad = float(input('''
---------------------------------------
LA CONSIGNACION TIENE QUE SER MAYOR A 0
---------------------------------------

Por favor ingrese un nuevo valor: '''))
                cuentas[llaveCuentas]['saldo'] += cantidad
                print('¡¡¡Consignacion exitosa!!!')
                # Utilizamos nuesta lista movimientos y le asignamos la cedula del usuario que quizo consignar
                # Para mantener identificado a que usuario en especifico pertenece ese movimiento
                movimientos[llaveMovimientos] = {
                    'numCuen': valor['numCuenta'],
                    'clav': valor['clave'],
                    'tipoMV': 'Consignacion a la cuenta', 
                    'referencia': referenciaConsignaciones, 
                    'descripcion': 'El usuario consignó dinero a su cuenta bancaria', 
                    'valor': '+' + str(cantidad),
                    'tiempo': datetime.datetime.today()}
                llaveMovimientos += 1
                referenciaConsignaciones *= 2
                
                break
        
        if not usuario_encontrado:
                ingreso = input('''
--------------------------------
EL DATO INGRESADO ES INCORRECTO
SELECCIONE NUEVAMENTE UNA OPCION
--------------------------------

(1). Ingresar con el numero de documento
(2). Ingresar con el numero de cuenta

''')
                
                if ingreso == '1':
                    doc = input('Ingrese su documento: ')
                if ingreso == '2':
                    num = input('Ingrese su numero de cuenta: ')




# La funcion retirar funciona exactamente igual que la funcion consignar
# La diferencia es que esta funcion no te permite retirar mas de lo que ya tienes en tu cuenta
# Y te informa el saldo actual de la cuenta
def retirar_dinero():
    global llaveMovimientos
    validado, numeroCuenta = ingreso()
    if validado:
        print('''
-------------------------------------------
--------------RETIRAR DINERO---------------
-------------------------------------------
''')
        for llaveCuentas, valor in cuentas.items():
            if str(llaveCuentas) == numeroCuenta:
                cantidad = float(input('Ingrese la cantidad que desea retirar: '))
                while cantidad > valor['saldo'] or cantidad <= 0:
                        cantidad = float(input(f'''
    ----------------------------
    FONDOS INSUFICIENTES
    SU SALDO ES DE: {cuentas[llaveCuentas]['saldo']}
    ----------------------------

    Porfavor ingrese un nuevo valor: '''))
                cuentas[llaveCuentas]['saldo'] -= cantidad
                print('¡¡¡Retiro exitoso!!')
                movimientos[llaveMovimientos] = {
                    'numCuen': valor['numCuenta'],
                    'clav': valor['clave'],
                    'tipoMV': 'Retiro a la cuenta', 
                    'referencia': 0, 
                    'descripcion': 'El usuario retiró dinero de su cuenta bancaria', 
                    'valor': '-' + str(cantidad),
                    'tiempo': datetime.datetime.today()}
                llaveMovimientos += 1




# la funcion pagar servicios funciona de una manera similar solo que incluye un menu adicional
# Y no te deja pagar un recibo si el monto a pagar es mayor al saldo de la cuenta
# Tambien te notifica si la opcion elegida no se encuentra dentro del rango establecido
def pagar_servicios():
    global llaveMovimientos
    validado, numeroCuenta = ingreso()
    if validado:
        for llaveCuentas, valor in cuentas.items():
            if str(llaveCuentas) == numeroCuenta:
                while True:
                    opcion = input('''
    ------------------------------------------
    ------SELECCIONE UNA DE LAS OPCIONES------
    ------------------------------------------

    (1). Pagar recibo de la energia.
    (2). Pagar recibo del agua.
    (3). Pagar recibo del gas.
    (0). Cerrar programa.

    ''')
                    match opcion:
                        case '1':
                            referencia = input('Ingrese la referencia del pago: ')
                            monto = float(input('Ingrese el monto a pagar: '))
                            while monto > valor['saldo'] or monto <= 0:
                                monto = float(input(f'''
    ----------------------------
    FONDOS INSUFICIENTES
    SU SALDO ES DE: {cuentas[llaveCuentas]['saldo']}
    ----------------------------

    Porfavor ingrese un nuevo valor: '''))
                            cuentas[llaveCuentas]['saldo'] -= monto
                            print('¡¡¡Pago exitoso!!!')
                            movimientos[llaveMovimientos] = {
                                    'numCuen': valor['numCuenta'],
                                    'clav': valor['clave'],
                                    'tipoMV': 'Pago de energia', 
                                    'referencia': referencia, 
                                    'descripcion': 'El usuario pagó el recibo de la energia', 
                                    'valor': '-' + str(monto),
                                    'tiempo': datetime.datetime.today()}
                            llaveMovimientos += 1
                        case '2':
                            referencia = input('Ingrese la referencia del pago: ')
                            monto = float(input('Ingrese el monto a pagar: '))
                            while monto > valor['saldo'] or monto <= 0:
                                monto = float(input(f'''
    ----------------------------
    FONDOS INSUFICIENTES
    SU SALDO ES DE: {cuentas[llaveCuentas]['saldo']}
    ----------------------------

    Porfavor ingrese un nuevo valor: '''))
                            cuentas[llaveCuentas]['saldo'] -= monto
                            print('¡¡¡Pago exitoso!!!')
                            movimientos[llaveMovimientos] = {
                                    'numCuen': valor['numCuenta'],
                                    'clav': valor['clave'],
                                    'tipoMV': 'Pago del agua', 
                                    'referencia': referencia, 
                                    'descripcion': 'El usuario pagó el recibo del agua', 
                                    'valor': '-' + str(monto),
                                    'tiempo': datetime.datetime.today()}
                            llaveMovimientos += 1
                        case '3':
                            referencia = input('Ingrese la referencia del pago: ')
                            monto = float(input('Ingrese el monto a pagar: '))
                            while monto > valor['saldo'] or monto <= 0:
                                monto = float(input(f'''
    ----------------------------
    FONDOS INSUFICIENTES
    SU SALDO ES DE: {cuentas[llaveCuentas]['saldo']}
    ----------------------------

    Porfavor ingrese un nuevo valor: '''))
                            cuentas[llaveCuentas]['saldo'] -= monto
                            print('¡¡¡Pago exitoso!!!')
                            movimientos[llaveMovimientos] = {
                                    'numCuen': valor['numCuenta'],
                                    'clav': valor['clave'],
                                    'tipoMV': 'Pago del gas', 
                                    'referencia': referencia, 
                                    'descripcion': 'El usuario pagó el recibo del gas', 
                                    'valor': '-' + str(monto),
                                    'tiempo': datetime.datetime.today()}
                            llaveMovimientos += 1
                        case '0':
                            print('Finalizando programa...')
                            break
                        case _:
                            print('''
            ------LA OPCION NO ESTA DENTRO DEL RANGO-------
            --INGRESE UN VALOR ENTRE (1-3). 0 PARA SALIR.--''')




# Esta funcion es sencilla, solo imprime todos los movimientos del usuario segun su numero de cuenta
def movimientos_bancarios():
    validado, numeroCuenta = ingreso()
    if validado:
        print(f'''
---------------------------------
------MOVIMIENTOS BANCARIOS------
---------------------------------''')
        for iterador, valor in movimientos.items():
            if str(valor["numCuen"]) == numeroCuenta:
                print(f'''

    Tipo de Movimiento: {valor['tipoMV']}
    Referencia: {valor['referencia']}
    Descripcion del Movimiento: {valor['descripcion']}
    Valor del Movimiento: {valor['valor']}
    Tiempo: {valor['tiempo']}''')

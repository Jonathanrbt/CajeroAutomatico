# AL diccionario cuentas se almacenan los usuarios donde cada usuario es un nuevo diccionario y la llave de cada uno
# Es su numero de cuenta
cuentas = {}
# Es un diccionario que Guarda todos los movimientos de dinero en el banco junto con sus propiedades
# Cada vez que se agrega un nuevo movimiento el valor aumenta en 1 
movimientos = {}
#Sirve para generar el numero de cuenta de cada usuario y nos dice cuantos usuarios tenemos registrados
#Despues de generar un numero al usuario el valor aumenta en 1
indice = 0  
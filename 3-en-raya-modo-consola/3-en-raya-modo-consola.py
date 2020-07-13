
# Para dar color y estilo a las letras se importó "colorama"
from colorama import  Fore, Style



# VARIABLES DEFINIDAS LAS CUALES SERÁN GLOBALES:

# La variable tablero es una Matriz la cual contiene la estructura del juego.
tablero = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# Esto indicará si el juego ha terminado o no.
Juego_continua = True

# Esta variable dirá el ganador.
ganador = None

# Esto indica quien juega primero, en este caso será la "x" para el primer jugador.
actual_jugador = "X"




# FUNCIONES:



# Esta función permite iniciar el juego.

import presentacion   # Esto sirve para importar el modulo presentacion.py

def iniciar_juego():# Esta funcion será la principal donde se va iniciar el juego.

    # Aqui se invoca a esta funcion para que muestre la presentacion y se introduzca el nombre de los jugadores.
    nombre_jugadores_e_intrucciones()


    # Aquí se llama a la funcion del tablero para que se muestre en pantalla.
    mostrar_tablero()

    # Este WHILE se detendrá hasta que el haya un ganador o un empate.
    while Juego_continua:
        # Se llama a esta funcion para que repita los turnos.
        turno(actual_jugador)

        # Se llama a esta funcion para que verifique si el juego a terminado.
        verificar_juego()

        # Al llamar esta funcion permitirá pasar el turno al otro jugador.
        cambio()

    # Estas CONDICIONALES, va a imprimir en pantalla al ganador o si hay un empate cuando el juego ha terminado.
    if ganador == "X" or ganador == "O":
        print("?  " + ganador + " ganó.")



    elif ganador == None:
        print("? Empate.")


    # Aqui va se establece los colores por cada archivo, mediante style y fore.
    print(Style.BRIGHT + Fore.LIGHTYELLOW_EX)

    # Se abre el archivo curso.txt mediante r que es en modo lectura
    archivo1 = open("curso.txt", "r")
    for cadena in archivo1:
        print(cadena)
    archivo1.close()
    print()

    # Se abre el archivo integrantes.txt mediante r que es en modo lectura
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX)
    archivo2 = open("integrantes.txt", "r")
    for cadena in archivo2:
        print(cadena)
    archivo2.close()
    print()

    # Se abre el archivo nota.txt mediante r que es en modo lectura
    print(Style.BRIGHT + Fore.LIGHTRED_EX)
    archivo3 = open("nota.txt", "r")
    for cadena in archivo3:
        print(cadena)
    archivo3.close()




# Esta funcion es del tablero para que se muestre en pantalla estableciendolo mediante las posiciones
def mostrar_tablero():
    print("\n")
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2] + "     1 | 2 | 3")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5] + "     4 | 5 | 6")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8] + "     7 | 8 | 9")
    print("\n")


# Esta funcion es para que al inicio se muestre como una presentacion y solicite los nombres de los jugadores.
def nombre_jugadores_e_intrucciones():

    jugador1 = input(Style.BRIGHT + Fore.LIGHTBLUE_EX +"? Ingrese el nombre del primer jugador: ")
    jugador2 = input(Style.BRIGHT + Fore.LIGHTBLUE_EX +"? Ingrese el nombre del segundo jugador: ")
    print()
    print(Style.BRIGHT + Fore.LIGHTCYAN_EX +"* INSTRUCCIONES:")
    print(Style.BRIGHT + Fore.WHITE +"   ? A el(la) jugador(a) 1 " + jugador1 + " le corresponde la  ' X ' .")
    print(Style.BRIGHT + Fore.WHITE +"   ? A el(la) jugador(a) 2 " + jugador2 + " le corresponde la  ' O ' .")
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX)

# Esta funcion se encarga de pedir la posicion y validarla.
def turno (jugador):

    # Aqui se obtiene la posicion
    print(Style.BRIGHT + Fore.WHITE + "? Turno de: " + jugador)
    posicion = input(Style.BRIGHT + Fore.WHITE +    "? Ingrese una posición desde 1-9: ")
    print(Style.BRIGHT + Fore.LIGHTBLUE_EX)
    # Aqui se va a validar la posicion ingresada.
    validar = False

    # Mientras no es válido se irá ejecutando el bucle WHILE.
    while not validar:

        # Acá mientras que la posicion ingresada no está en la lista, se irá pidiendo que se ingrese la posicion mediante el WHILE.
        while posicion not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            posicion = input(Style.BRIGHT + Fore.WHITE +"? Ingrese una posición desde 1-9: ")
            print(Style.BRIGHT + Fore.LIGHTBLUE_EX)
        # Aqui obtiene el indice validado que está dentro de la lista.
        posicion = int(posicion) - 1

        # Para asegurar que la posicion validada ingresada esté disponible en el tablero. se usa condicionales.
        if tablero[posicion] == "-":
            validar = True
        else:
            print(Style.BRIGHT + Fore.LIGHTRED_EX +"? Posición no válida. Intenta de nuevo.")
            print(Style.BRIGHT +  Fore.LIGHTBLUE_EX)
    # Se coloca la posicion para que se muestre en el tablero.
    tablero[posicion] = jugador

    # Se muestra el tablero.
    mostrar_tablero()


# Esta funcion comprueba si el juego ha terminado
def verificar_juego():
    verificar_ganador()
    verificar_empate()


# Esta funcion verifica si alguien ha ganado.
def verificar_ganador ():
    # Se invoca a la variable de manera global
    global ganador
    # Aqui se verifica si hubo un ganador
    ganador_fila = comprobar_filas()
    ganador_columna = comprobar_columnas()
    ganador_forma_diagonal = comprobar_diagonales()
        # Aqui se obtiene el ganador
    if ganador_fila:
        ganador = ganador_fila
    elif ganador_columna:
        ganador = ganador_columna
    elif ganador_forma_diagonal:
        ganador = ganador_forma_diagonal
    else:
        ganador = None


# Esta funcion revisa las filas para determinar si hay un ganador
def comprobar_filas():
    # Se llama a una variable mediante global.
    global Juego_continua
    # Aquí se comprueba si alguna de las filas tiene el mismo valor (y no está vacía)
    fila_1 = tablero[0] == tablero[1] == tablero[2] != "-"
    fila_2 = tablero[3] == tablero[4] == tablero[5] != "-"
    fila_3 = tablero[6] == tablero[7] == tablero[8] != "-"
    # Aquí si alguna fila tiene una coincidencia o es igual mejor dicho, indica que hay una victoria.
    if fila_1 or fila_2 or fila_3:
        Juego_continua = False
    # Se retorna el ganador:
    if fila_1:
        return tablero[0]
    elif fila_2:
        return tablero[3]
    elif fila_3:
        return tablero[6]
    # O retorna ninguno en el caso de que no hay concidencias, es decir, un ganador.
    else:
        return None


# Esta funcion revisa las columnas para determinar si hay un ganador
def comprobar_columnas():
    # Se llama a una variable mediante global.
    global Juego_continua
    # Aquí se comprueba si alguna de las columnas tiene el mismo valor (y no está vacía)
    columna_1 = tablero[0] == tablero[3] == tablero[6] != "-"
    columna_2 = tablero[1] == tablero[4] == tablero[7] != "-"
    columna_3 = tablero[2] == tablero[5] == tablero[8] != "-"
    # Aquí si alguna columna es igual , entonces indica que hay una victoria.
    if columna_1 or columna_2 or columna_3:
        Juego_continua = False
    # Se retorna el ganador:
    if columna_1:
        return tablero[0]
    elif columna_2:
        return tablero[1]
    elif columna_3:
        return tablero[2]
    # O retorna ninguno en el caso de que no hay coincidencias, es decir, un ganador.
    else:
        return None


# Esta funcion revisa las diagonales para determinar si hay un ganador
def comprobar_diagonales():
    # Se llama a una variable mediante global.
    global Juego_continua
    # Aquí se comprueba si alguna de las diagonales tiene el mismo valor (y no está vacía)
    diagonal_1 = tablero[0] == tablero[4] == tablero[8] != "-"
    diagonal_2 = tablero[2] == tablero[4] == tablero[6] != "-"
    # Aquí si alguna diagonal es igual , entonces indica que hay una victoria.
    if diagonal_1 or diagonal_2:
        Juego_continua = False
    # Se retorna el ganador:
    if diagonal_1:
        return tablero[0]
    elif diagonal_2:
        return tablero[2]
    # O retorna ninguno en el caso de que no hay concidencias, es decir, un ganador.
    else:
        return None


# Esta funcion determina si hay un empate o no.
def verificar_empate():
    # Se llama a la variable mediante global
    global Juego_continua
    # Si el tablero esta lleno, se determina como verdadero el cual indica que no hay un ganador, es decir, hay empate
    if "-" not in tablero:
        Juego_continua = False
        return True
    # Sino, retorna falso para indicar que no hay un empate.
    else:
        return False


# Esta funcion cambia las variables de X a O,o, viceversa.
def cambio():
    # Se llama a las variable necesaria con global.
    global actual_jugador
    # Aca si el jugador actual era X, lo convierta a O.
    if actual_jugador == "X":
        actual_jugador = "O"
    # O si el jugador actual era X, lo convierta a O.
    elif actual_jugador == "O":
        actual_jugador = "X"


# Aqui se llama a esta funcion para poder empezar a jugar.
iniciar_juego()
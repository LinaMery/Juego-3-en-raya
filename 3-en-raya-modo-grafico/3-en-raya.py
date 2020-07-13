from tkinter import *                   # SE IMPORTA TKINTER
from tkinter import messagebox         # SE IMPORTA MESSAGEBOX PARA CREAR MENSAJES DE TEXTO
from tkinter import simpledialog       # SE IMPORTA SIMPLEDIALOG PARA CREAR PEQUEÑOS DIÁLOGOS

def bloquear_botones(): # Esta función sirve para bloquear los botones al iniciar el juego.
    for i in range(0,9):
        lista_botones[i].config(state="disable") # aqui es donde se configura el estado de los botones y se pone en inhabilitado.




def iniciarJuego(): # Esta función sirve para desbloquear los botones una vez recibido el mensaje de iniciar juego.
    for i in range(0,9):
        lista_botones[i].config(state="normal") # Esto cambia el estado de los botones y los habilita, lo cual va a permitir dar click a los botones
        lista_botones[i].config(bg="#B5E3DC")   # Esto cambia el color de los botones al dar click al iniciar el juego.
        lista_botones[i].config(text="")        # Esto configura para que el texto que tiene cada boton esté vacio despues de jugar el programa.
        t[i] = "N"                              # Esto limpia el tablero interno, N esta declarado como vacio
    global NombreJugador1,NombreJugador2        # Global se encarga de llamar a las variables de los jugadores, haciendo que reconozca estas variables global y sepa que se está referiendo a ello para poder acceder.
    NombreJugador1 = simpledialog.  askstring("Gamers","Escribe el nombre del 1er jugador: ") # Aqui sirve para recibir los parámetros mediante asktring que es quien pide la cadena a ingresar. Todoo ello dentro de un dialogo
    NombreJugador2 = simpledialog.askstring("Gamers","Escribe el nombre del 2do jugador: ")
    turno_jugador.set("TURNO: " + NombreJugador1)  # Esto sirve para mostrar el primer turno, el cual le corresponde al jugador 1.



def cambiar(num):
    global turno,NombreJugador1,NombreJugador2              # Aqui se accede a las variables globales, turno para cambiar el turno a quien le corresponde, el jugador 1 y 2 para que lo muestre.
    if t[num] == "N" and turno ==0:                         # Aqui se indica que cuando el jugador 1 de click en los botones, entonces:
        lista_botones [num].config(text="X",font=('Helvetica',9, 'bold'))   # muestra la X en el boton donde se dió click
        lista_botones [num].config(bg="lightgreen")                         # cambia el color del boton
        t [num] = "X"                                                       # aqui se indica que ya hay algo dentro de ese boton
        turno = 1                                                           # aqui se cambia a 1 para que indique que le toca a otro jugador
        turno_jugador.set("TURNO: " + NombreJugador2)                       # aqui se cambia la etiqueta para que se muestre e indique que le toca al jugador 2 # El "set" indica que se está accediendo a un stringvar
    elif t [num] == "N" and turno == 1:
        lista_botones[num].config(text="O",font=('Helvetica',9, 'bold'))    #aqui se aplica lo mismo solo que se cambia para que sea para el jugador 2
        lista_botones[num].config(bg="#47ADF3")
        t [num] = "O"
        turno = 0
        turno_jugador.set("Turno: " + NombreJugador1)
    lista_botones[num].config(state="disable")              #aqui se indica que cuando un jugador dió click en un boton, pues este se convierta en inhabilitado para que ya no puedan darle otro click.
    resultado_del_juego()                                   # aqui se manda una funcion que permita verificar que jugador a ganado


# Esta funcion va a determinar que jugador gana # Se determina mediante condicionales que indican todas las posibilidades para que gane un jugador, ya sea en forma horinzontal, vertical y diagonal.
def resultado_del_juego():
    if (t[0] == "X" and t[1] == "X" and t[2] == "X") or (t[3] == "X" and t[4] == "X" and t[5] == "X") or (t[6] == "X" and t[7] == "X" and t[8] == "X"):
        bloquear_botones()
        messagebox.showinfo("Ganador","Oh!! ganó " + NombreJugador1 + ". Dale en aceptar y click abajo para jugar la revancha!!.. "+NombreJugador2 +" no te dejarás ganar cierto!! ") # si se da esta condicion, entonces va a mostrar un mensaje diciendo que ganó el jugador 1
    elif (t[0] == "X" and t[3] == "X" and t[6] == "X") or (t[1] == "X" and t[4] == "X" and t[7] == "X") or (t[2] == "X" and t[5] == "X" and t[8] == "X"):
        bloquear_botones()
        messagebox.showinfo("Ganador","Oh!! ganó " + NombreJugador1+". Dale en aceptar y click abajo para jugar la revancha!!.. "+NombreJugador2 +" no te dejarás ganar cierto!! ")# si se da esta condicion, entonces va a mostrar un mensaje diciendo que ganó el jugador 1
    elif (t[0] == "X" and t[4] == "X" and t[8] == "X") or (t[2] == "X" and t[4] == "X" and t[6] == "X"):
        bloquear_botones()
        messagebox.showinfo("Ganador","Oh!! ganó " + NombreJugador1+ ". Dale en aceptar y click abajo para jugar la revancha!!.. "+NombreJugador2 +" no te dejarás ganar cierto!! ")# si se da esta condicion, entonces va a mostrar un mensaje diciendo que ganó el jugador 1
    elif (t[0] == "O" and t[1] == "O" and t[2] == "O") or (t[3] == "O" and t[4] == "O" and t[5] == "O") or (t[6] == "O" and t[7] == "O" and t[8] == "O"):
        bloquear_botones()
        messagebox.showinfo("Ganador","Oh!! ganó " + NombreJugador2+ ". Dale en aceptar y click abajo para jugar la revancha!!.. "+NombreJugador1 +" no te dejarás ganar cierto!! ")# si se da esta condicion, entonces va a mostrar un mensaje diciendo que ganó el jugador 2
    elif (t[0] == "O" and t[3] == "O" and t[6] == "O") or (t[1] == "O" and t[4] == "O" and t[7] == "O") or (t[2] == "O" and t[5] == "O" and t[8] == "O"):
        bloquear_botones()
        messagebox.showinfo("Ganador","Oh!! ganó " + NombreJugador2+   ". Dale en aceptar y click abajo para jugar la revancha!!.. "+NombreJugador1 +" no te dejarás ganar cierto!! ")# si se da esta condicion, entonces va a mostrar un mensaje diciendo que ganó el jugador 2
    elif (t[0] == "O" and t[4] == "O" and t[8] == "O") or (t[2] == "O" and t[4] == "O" and t[6] == "O"):
        bloquear_botones()
        messagebox.showinfo("Ganador","Oh!! ganó " + NombreJugador2+ ". Dale click abajo para jugar la revancha!!")# si se da esta condicion, entonces va a mostrar un mensaje diciendo que ganó el jugador 2


# Ventana del juego
ventana = Tk()                                          # Tk es un constructor de tkinter
ventana.geometry("380x380")                             # geometry sirva para diseñar el tamaño de la ventana
ventana.title("BIENVENIDO AL JUEGO DEL 3 EN RAYA")      # acá se colo el nombre de la ventana insertando "title"
turno = 0                                               # esta variable va a indicar el turno a quien le corresponde jugar.


imagen = PhotoImage(file="fondo.gif")                   # aqui se inserta la imagen
Label(ventana, image=imagen, bd=0).pack(side="left")




NombreJugador1 = ""            # Aqui se va a pedir los nombres del jugador 1 y 2
NombreJugador2 = ""

lista_botones = []             # Se crea una lista que va a almacenar los botones
t = [] #  X O N                # Esta lista sirve para controlar el contenido en donde hay una X y O, o N que es simplemente donde no hay Nada
turno_jugador = StringVar()    # Sirve para indicar  el turno del jugador o a quien le toca
for i in range (0,9):       # Aca crea el rango de los botones que inicia 
    t.append("N")


# Aqui se crea los botones del 0 al 8 :
boton_0 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(0))  # Se crea un boton que está dentro de la ventana, poniendo el hancho y alto, y su color
lista_botones.append(boton_0)                                                       # aqui al dar clikc, el boton se agrega a la  lista_botones
boton_0.place(x=75,y=90)                                                            # aquí se coloca la ubicacion mediante,  x = horizontal, y = vertical
                                                                                    # todoo ello se realiza mediante la funcion lambda que está sin parámetros, y cuando se le da click al boton 0, lambda recibe el parametro cambiar(0) para que se muestre.

boton_1 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(1))
lista_botones.append(boton_1)
boton_1.place(x=150,y=90)

boton_2 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(2))
lista_botones.append(boton_2)
boton_2.place(x=225,y=90)

boton_3 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(3))
lista_botones.append(boton_3)
boton_3.place(x=75,y=148)

boton_4 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(4))
lista_botones.append(boton_4)
boton_4.place(x=150,y=148)

boton_5 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(5))
lista_botones.append(boton_5)
boton_5.place(x=225,y=148)

boton_6 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(6))
lista_botones.append(boton_6)
boton_6.place(x=75,y=206)

boton_7 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(7))
lista_botones.append(boton_7)
boton_7.place(x=150,y=206)

boton_8 = Button(ventana,width=9,height=3,bg="#F3AF47",command=lambda: cambiar(8))
lista_botones.append(boton_8)
boton_8.place(x=225,y=206)


# Se crea una etiqueta que va a indicar el turno a quien le corresponde y para ello se llama a la variable "turno_jugador"
turnoEtiqueta = Label(ventana,textvariable=turno_jugador).place(x=68,y=55)

# Se crea un boton para hacer click e iniciar el juego. fb = color de letra, bg = color del boton, font = tipo,tamaño,y clase de la letra.
inicio = Button(ventana,bg="#18A1B9",fg="black",text="Click aquí para jugar!!",font=("Verdana",12,'bold'),width=50,height=2,command=iniciarJuego).place(x=-93,y=300) # dentro de ello se crea un comando el cual va a mandar a llamar una funcion para que inicie el juego.

bloquear_botones() # Esta funcion se llama aqui despues de haber creado el interfaz
ventana.mainloop()








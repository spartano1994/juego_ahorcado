


from src.screen import *
from src.words import *

def jugar():
    palabra = seleccionar_palabra()
    

def run():

    portada()

    dificultad = "Fácil"
    importar_palabras( dificultad ) 

    while True :
        opcion = pantalla_menu( dificultad )

        if opcion == 1 :
            jugar() 
        elif opcion == 2:
            dificultad = pantalla_dificultad()
            importar_palabras( dificultad ) 
        elif opcion == 3:
            pantalla_puntuacion()
        elif opcion == 4:
            pantalla_acerca_de()
        else:
            pantalla_salida()
            break


if __name__ == "__main__":
    run()
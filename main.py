from src.screen import *
from src.words import *
from src.score import *

def jugar( palabras = [] , dificultad = "Fácil" , puntos = 0 ):
    
    
    palabra  = seleccionar_palabra( palabras )
    palabra_secreta = PalabraSecreta( palabra )

    puntos , intentos = puntos_por_palabra( longitud = len( palabra ) , nivel = dificultad )

    while intentos > 0 :
        while True :
            print( palabra_secreta )
            try:
                letra = input( "Introduzca una letra: " ).strip().lower()
                break
            except:
                print( "Introduce un caracter válido..." )
                time.sleep( 2 ) 
                os.system( "cls" )

        acierto = palabra_secreta.descubrir_letra( letra )

        finalizar = palabra_secreta.validar_cadenas()

        if finalizar:
            return puntos


        if not acierto:
            intentos -= 1
        
        os.system( "cls" )
    
    return 
            

    


def run():
    portada()

    dificultad = "Fácil"
    lista_palabras = importar_palabras( dificultad ) 

    while True :
        opcion = pantalla_menu( dificultad )

        if opcion == 1 :
            jugar( dificultad , palabras = lista_palabras.to_list() , puntos = 0 ) 
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
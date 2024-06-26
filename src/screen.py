import os
import time


def impresion_barrida( lista , tiempo_transicion = 0.1 , borrar = False , espera_final = 0 ) :
    for element in lista :
        print( element )
        time.sleep( tiempo_transicion )

    time.sleep( espera_final )  
    
    if borrar == True :
        os.system( "cls" )
        

def portada():
    texto_bienvenido = [ " 888888ba  oo                                              oo       dP                      dP" ,
                        " 88    `8b                                                          88                      88 ",
                        " 88aaaa8P' dP .d8888b. 88d888b. dP   .dP .d8888b. 88d888b. dP .d888b88 .d8888b.    .d8888b. 88 ",
                        " 88   `8b. 88 88ooood8 88'  `88 88   d8' 88ooood8 88'  `88 88 88'  `88 88'  `88    88'  `88 88 ",
                        " 88    .88 88 88.  ... 88    88 88 .88'  88.  ... 88    88 88 88.  .88 88.  .88    88.  .88 88 ",
                        " 88888888P dP `88888P' dP    dP 8888P'   `88888P' dP    dP dP `88888P8 `88888P'    `88888P8 dP " ,
                        "\n",
                        "            oo                                              dP          dP          ",
                        "                                                            88          88          ",
                        "            dP dP    dP .d8888b. .d8888b. .d8888b.    .d888b88 .d8888b. 88          ",
                        "            88 88    88 88ooood8 88'  `88 88'  `88    88'  `88 88ooood8 88          ",
                        "            88 88.  .88 88.  ... 88.  .88 88.  .88    88.  .88 88.  ... 88          ",
                        "            88 `88888P' `88888P' `8888P88 `88888P'    `88888P8 `88888P' dP 88 88 88 ",
                        "            88                        .88                                           ",
                        "            dP                    d8888P                                            "
                    ]
    
    titulo_juego = ["\n\n\n\n",
                    "          ###    ##     ##  #######  ########   ######     ###    ########   #######  " ,
                    "         ## ##   ##     ## ##     ## ##     ## ##    ##   ## ##   ##     ## ##     ## " ,
                    "        ##   ##  ##     ## ##     ## ##     ## ##        ##   ##  ##     ## ##     ## " ,
                    "       ##     ## ######### ##     ## ########  ##       ##     ## ##     ## ##     ## " ,
                    "       ######### ##     ## ##     ## ##   ##   ##       ######### ##     ## ##     ## " ,
                    "       ##     ## ##     ## ##     ## ##    ##  ##    ## ##     ## ##     ## ##     ## " ,
                    "       ##     ## ##     ##  #######  ##     ##  ######  ##     ## ########   #######  ",
                    "\n\n\n\n" ]
    
    os.system( "cls" )
    impresion_barrida( lista = texto_bienvenido , borrar = True , espera_final = 1 )
    impresion_barrida( titulo_juego, espera_final = 1.5 )
    input( "\t\t\t\t\tPresiona enter\t\t" )
    os.system( "cls" )


def pantalla_menu( dificultad = "Fácil"):
    menu_principal = [ "Selecciona una opción:" ,
                      "\t1.-Jugar" ,
                      f"\t2.-Dificultad ( {dificultad} )" ,
                      "\t3.-Puntuaciones" ,
                      "\t4.-Acerca de" ,
                      "\t5.-Salir del juego"]
    
    while True :
        impresion_barrida( menu_principal , tiempo_transicion = 0 )

        try:
            opcion = int( input( "\tOpción: " ) )
            return opcion
        except:
            print( "Debes digitar una opción válida, intenta de nuevo..." )
            
        time.sleep( 1.5 )
        os.system( "cls" )


def pantalla_dificultad():
        menu_dificultad = [ "Selecciona el nivel de dificultad:" ,
                      "\t1.-Muy Fácil" ,
                      f"\t2.-Fácil" ,
                      "\t3.-Normal" ,
                      "\t4.-Dificil" ,
                      "\t5.-Maestro" ]
        
        impresion_barrida( menu_dificultad , tiempo_transicion = 0 )

        


def pantalla_puntuacion():
    pass


def pantalla_acerca_de():
    pass


def pantalla_salida():
    pass

if __name__ == "__main__":
    pass
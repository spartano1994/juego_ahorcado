
import csv
import time
import os
import pathlib
import numpy as np
import pandas as pd

def quitar_acentos( palabra ) :
    palabra = palabra.replace( "á" , "a" )
    palabra = palabra.replace( "é" , "e" )
    palabra = palabra.replace( "í" , "i" )
    palabra = palabra.replace( "ó" , "o" )
    palabra = palabra.replace( "ú" , "u" )

    return palabra

def importar_palabras( nivel ):
    archivo_texto = quitar_acentos( nivel.lower() + ".csv" )

    path = pathlib.Path( "./dictionary/" + archivo_texto )

    if os.path.exists( path ):
        df = pd.read_csv( path , encoding = "utf8")
        palabras_del_nivel = df[ nivel ]

        return palabras_del_nivel

    else:#pendiente
        data = [ [ "Muy Fácil" , "Fácil" , "Normal" , "Dificil" , "Maestro" ] ,
                [ 1 , 2 , 3 , 4 , 5 ] ]
        
        with open( path , mode = "w" , encoding = "utf8" , newline = "" ) as archivo :
            writer = csv.writer( archivo )

            for row in data :
	            writer.writerow( row )


def seleccionar_palabra( palabras ):
    palabra_elegida = np.random.choice( palabras )
    print( palabra_elegida )


class PalabraSecreta( object ) :
    def __init__( self  , palabra ):
        self.__palabra = palabra
        self.palabra_oculta = self.cubrir_palabra( self.__palabra )

    def cubrir_palabra( self , palabra ) :
        cadena_oculta = "".join( [ "_" for _ in palabra ] )
        return cadena_oculta

    def descubrir_letra( self , letra = "" ) :
        cadena = self.__palabra 

        if letra not in cadena :
            return False

        nueva_palabra_oculta = ""
        longitud_palabra = len( cadena )

        for i in range( longitud_palabra ) :
            if cadena[ i ] == letra[ 0 ] :
                nueva_palabra_oculta += letra[ 0 ]
            else :
                nueva_palabra_oculta +=  self.palabra_oculta[ i ]
                
        self.palabra_oculta = nueva_palabra_oculta

        return True

    def validar_cadenas( self ):
        if self.__palabra == self.palabra_oculta :
            return True
        return False

    def __str__( self ) :
        return ( " ".join( list( self.palabra_oculta ) ) )
    

if __name__ == "__main__":
    pass
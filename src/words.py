
import random as rn


def importar_palabras( nivel ):
    return []

def seleccionar_palabra():
    return


class PalabraSecreta( object ) :
    def __init__( self  , palabra ):
        self.__palabra = palabra
        self.palabra_oculta = self.cubrir_palabra( self.__palabra )

    def cubrir_palabra( self , palabra ) :
        cadena_oculta = "".join( [ "_" for letra in palabra ] )
        return cadena_oculta

    def descubrir_letra( self , letra = "" ) :
        cadena = self.__palabra 

        if letra not in cadena :
            return False

        nueva_palabra_oculta = ""
        longitud_palabra = len( cadena )

        for i in range( longitud_palabra ) :
            if cadena[ i ] == letra :
                nueva_palabra_oculta += letra
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
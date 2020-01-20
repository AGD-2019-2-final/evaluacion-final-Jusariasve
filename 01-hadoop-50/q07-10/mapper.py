import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":

    ##
    ## itera sobre cada linea de codigo recibida
    ## a traves del flujo de entrada
    ##
    for line in sys.stdin:

        ##
        ## genera las tuplas palabra \tabulador 1
        ## ya que es un conteo de palabras
        ##
        word = line.split("   ")[0]
        value = int(line.split("   ")[2])
        value = "{:03.0f}".format(value)
        sys.stdout.write("{},{},{}".format(word,value,line))

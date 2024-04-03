#
# LeggiScriviFile.py - esempio di scrittura su un file e di lettura dallo stesso file
#

f = open("LeggiScriviFile.txt", "w")
for i in range(10):
    f.write( str(i+1) + ") Frase scritta dal programma sul file\n")
f.close()

g = open("LeggiScriviFile.txt", "r")
s = g.read()
g.close()

# stampa tutto il contenuto del file letto
print( "Stampa del contenuto del file [" + str(len(s)) + " bytes]:\n" )
print(s)

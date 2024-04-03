#
# si sposta e disegna un quadrato al centro, ciclando per i 4 lati
#

import turtle

turtle.penup()
turtle.goto(-50,-50)
turtle.pendown()

for i in range(4):
    turtle.forward(100)
    turtle.left(90)

input("Premere INVIO per chiudere il programma ...")
turtle.bye()
quit()

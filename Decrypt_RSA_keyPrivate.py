

#vamos a descifrar un mensaje C con la clave privada y el modulo N. 

#C = M^e mod N #C es el mensaje cifrado, M es el mensaje en claro, e es la clave publica y N es el modulo
#M = C^d mod N #M es el mensaje en claro, C es el mensaje cifrado, d es la clave privada y N es el modulo

n = 882564595536224140639625987659416029426239230804614613279163
e = 65537 #es el numero de Fermat más implementado en RSA como exponente. 
c = 77578995801157823671636298847186723593814843845525223303932 #mensaje cifrado

#la clave privada que habiamos calculado del ejercicio anterior era: 
d = 121832886702415731577073962957377780195510499965398469843281

#ahora vamos a descifrar el mensaje C con la clave privada y el modulo N.
mensaje = pow(c,d,n)
print("mensaje descifrado: ", mensaje)


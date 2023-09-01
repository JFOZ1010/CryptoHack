#Author: JF0x0r
#recordemos que la forma de poder calcular la clave privada en RSA es calculando el inverso
#entre la clave publica que sabemos que es el numero de fermat 65537 y el modulo Phi n que es: 
#phi(n) = (p-1)*(q-1) siendo p y q los dos numeros primos que hemos utilizado para calcular el modulo n.

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
phi = (p-1)*(q-1)
d = pow(e, -1, phi)
print(d)


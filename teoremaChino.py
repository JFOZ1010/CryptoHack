
"""
En esta función hare la solución al problema del teorma chino de los restos, 
el cual se refiere a que si tenemos un sistema de congruencias de la forma:
x ≡ a1 (mod n1) , x ≡ a2 (mod n2) , ... , x ≡ ak (mod nk) hasta poder cumplir con k congruencias
en este caso que se cumpla que a tal que x ≡ a mod 935. 
"""

def factorizar(n): 
    factores = []
    i = 2
    while i * i <= n: 
        if n % i: 
            i += 1
        else: 
            n //= i 
            factores.append(i) 
    if n > 1: 
        factores.append(n) 
    return factores


def teoremaChino(): 

    x = 0
    a = 0
    n = 935

    #factorizamos p en sus factores primos
    factores = factorizar(n)
    print(factores) 

    #ahora necesitamos establecer las congruencias de la forma x ≡ a mod n

    #5
    x = a % factores[0]
    m1 = 935//factores[0]
    print(f"m1 = {m1}")
    m1_inv = pow(m1, -1, factores[0])
    print(f"m1_inv = {m1_inv}")

    #en este caso entonces a1 = m1_inv * x % factores[0]
    #a1 = m1_inv * x * a % factores[0]

    #11
    x = a % factores[1]
    m2 = 935//factores[1]
    print(f"m2 = {m2}")
    m2_inv = pow(m2, -1, factores[1])
    print(f"m2_inv = {m2_inv}")
    #a2 = m2_inv * x * a % factores[1]

    #17
    x = a % factores[2]
    m3 = 935//factores[2]
    print(f"m3 = {m3}")
    m3_inv = pow(m3, -1, factores[2])
    print(f"m3_inv = {m3_inv}")
    #a3 = m3_inv * x * a % factores[2]

    #print(f"a1 = {a1}")
    #print(f"a2 = {a2}")
    #print(f"a3 = {a3}")


if __name__ == "__main__":
    teoremaChino()
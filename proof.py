from sympy.ntheory.modular import solve_congruence

# Datos dados
congruences = [(2, 5), (3, 11), (5, 17)]
N = 935

# Aplicar el Teorema Chino del Resto
result = solve_congruence(*congruences)

# Encontrar el valor a tal que x ≡ a mod 935
a = result[0] % N

print("El valor de a es:", a)

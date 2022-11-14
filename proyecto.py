# Proyecto 2 Funciones Lambda

cero = lambda f: lambda x: x
uno = lambda f: lambda x: f(x)
dos = lambda f: lambda x: f(f(x))
tres = lambda f: lambda x: f(f(f(x)))
cuatro = lambda f: lambda x: f(f(f(f(x))))
cinco = lambda f: lambda x: f(f(f(f(f(x)))))
seis = lambda f: lambda x: f(f(f(f(f(f(x))))))


#Operaciones
sucesor = lambda n: lambda f: lambda x: f(n(f)(x))


# Operaciones 2
alpha = lambda x: x + 1
beta = lambda x: 2 * x

#Resultado numeros 
print(uno(alpha)(0))
print(dos(alpha)(0))
print(tres(alpha)(0))
print(cuatro(alpha)(0))
print(cinco(alpha)(0))
print(seis(alpha)(0))



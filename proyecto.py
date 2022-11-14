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
suma = lambda a: lambda b: lambda f: lambda x: a(f)(b(f)(x))
multiplicacion = lambda a: lambda b: lambda f: lambda x: a(b(f))(x)
potencia = lambda a: lambda b: lambda f: lambda x: b(a)(f)(x)

# Operaciones 2
alpha = lambda x: x + 1
beta = lambda x: 2 * x

#Resultado numeros 
print("\nPruba numeros con alpha")
print(uno(alpha)(0))
print(dos(alpha)(0))
print(tres(alpha)(0))
print(cuatro(alpha)(0))
print(cinco(alpha)(0))
print(seis(alpha)(0))

#Pruebas con alpha
print("\nPruebas alpha")
print("Sucesor de: " + str(tres(alpha)(0)) + " es igual a : "+str(sucesor(tres)(alpha)(cero(alpha)(0))))
print("Suma de 2 + 4 = " + str(suma(dos)(cuatro)(alpha)(cero(alpha)(0))))
print("Multiplicacion de 6 * 5 = " + str(multiplicacion(seis)(cinco)(alpha)(cero(alpha)(0))))
print("Potencia de 2 ^ 3 = " + str(potencia(dos)(tres)(alpha)(cero(alpha)(0))))


#Pruebas con beta
print("\nPrubas beta")
print("Sucesor de: " + str(tres(beta)(0)) + " es igual a : "+str(sucesor(tres)(beta)(cero(beta)(0))))
print("Suma de 2 + 4 = " + str(suma(dos)(cuatro)(beta)(cero(beta)(0))))
print("Multiplicacion de 6 * 5 = " + str(multiplicacion(seis)(cinco)(beta)(cero(beta)(0))))
print("Potencia de 2 ^ 3 = " + str(potencia(dos)(tres)(beta)(cero(beta)(0))))



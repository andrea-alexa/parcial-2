'''Escribe un programa que, al recibir como dato un número entero positivo N, calcule el resultado de la siguiente serie:

1 + (1/2) + (1/3) + (1/4) + ... + (1/N) donde N es el número que el usuario ingrese

Si el usuario escribe un número incorrecto, el programa no se ejecuta. En cambio, pregunta de nuevo por la información hasta que el dato ingresado sea correcto. 
'''

print("==============================")
print("Bienvenido al prgrama")
print("===============================")

print("Programa iniciado")

while True:
    N = input("ingresa el numero: ")
    if N.isdigit() and int(N) >0:
        N= int(N)
        break
    else:
        print("DEBES INGRESAR UN NUMERO POSITIVO")
suma= 0
for i in range(1,N+1):
    suma+= 1/i
print(f" La suma de la serie hasta 1/{N} es {suma}")

print(" Fin del programa")

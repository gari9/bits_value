
# Calcular cuantos bits se necesitan para representar un numero
# Representacion binaria de un numero

# Introduciendo un valor por teclado


# Ingresando un valor por teclado
a = int(input("Ingrese un numero: "))

# Imprimiendo el valor ingresado en decimal
print("El numero es: ",a)

# Imprimiendo el valor ingresado en forma binaria
print("El numero en binario es: ",bin(a))

# Se necesita la funcion bit_length() para saber cuantos bits se necesitan para representar un numero
print("Se necesitan:",a.bit_length(),"bits para representar el numero") 


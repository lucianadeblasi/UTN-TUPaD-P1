# Práctico 1: Estructuras secuenciales - TUPaD
# Alumna: DEBLASI Luciana

# 1
print("Hola Mundo!")

# 2
# Pedir al usuario su nombre
nombre = input("¿Cuál es tu nombre? ")

# Imprimir el saludo utilizando f-string
print(f"Hola {nombre}!")

# 3
# Pedir al usuario los datos
nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = input("¿Cuántos años tienes? ")
residencia = input("¿Dónde vives? ")

# Imprimir la oración con los datos
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# 4
import math

# Pedir al usuario el radio del círculo
radio = float(input("¿Cuál es el radio del círculo? "))

# Calcular el área y el perímetro
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio

# Imprimir el resultado
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

# 5
# Pedir al usuario la cantidad de segundos
segundos = int(input("¿Cuántos segundos quieres convertir a horas? "))

# Convertir segundos a horas
horas = segundos / 3600

# Imprimir el resultado
print(f"{segundos} segundos equivale a {horas} horas.")

# 6
# Pedir al usuario un número
numero = int(input("¿De qué número quieres ver la tabla de multiplicar? "))

# Imprimir la tabla de multiplicar
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# 7
# Pedir al usuario dos números enteros distintos de 0
numero1 = int(input("Introduce el primer número entero (distinto de 0): "))
numero2 = int(input("Introduce el segundo número entero (distinto de 0): "))

# Verificar que los números son distintos de 0
if numero1 != 0 and numero2 != 0:
    # Realizar las operaciones
    suma = numero1 + numero2
    resta = numero1 - numero2
    multiplicacion = numero1 * numero2
    if numero2 != 0:  # Comprobar que no se intenta dividir por 0
        division = numero1 / numero2
        print(f"{numero1} + {numero2} = {suma}")
        print(f"{numero1} - {numero2} = {resta}")
        print(f"{numero1} * {numero2} = {multiplicacion}")
        print(f"{numero1} / {numero2} = {division}")
else:
    print("Los números deben ser distintos de 0.")

# 8
# Pedir al usuario su peso y altura
peso = float(input("¿Cuál es tu peso en kg? "))
altura = float(input("¿Cuál es tu altura en metros? "))

# Calcular el IMC
imc = peso / (altura ** 2)

# Imprimir el resultado
print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")

# 9
# Pedir al usuario la temperatura en grados Celsius
celsius = float(input("Introduce la temperatura en grados Celsius: "))

# Convertir a Fahrenheit
fahrenheit = (9/5) * celsius + 32

# Imprimir el resultado
print(f"La temperatura en Fahrenheit es: {fahrenheit:.2f}")

# 10
# Pedir al usuario tres números
numero1 = float(input("Introduce el primer número: "))
numero2 = float(input("Introduce el segundo número: "))
numero3 = float(input("Introduce el tercer número: "))

# Calcular el promedio
promedio = (numero1 + numero2 + numero3) / 3

# Imprimir el resultado
print(f"El promedio de los tres números es: {promedio:.2f}")

#mi primer cambio
#Punto 1
print ("Hola mundo")

#Punto 2
nombre = input("Por favor, ingresa tu nombre: ")
print (f"Hola {nombre}!")

#Punto 3
nombre = input("Por favor, ingresa tu nombre: ")
apellido = input("Por favor, ingresa tu apellido: ")
edad = input("Por favor, ingresa tu edad: ")
residencia = input("Por favor, ingresa tu lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Punto 4
import math
radio= float(input("Por favor, ingresa el radio del círculo: "))
area= math.pi * (radio ** 2)
perimetro= 2* math.pi * radio
print (f"El área del círculo es: {area}  ")
print (f"El perímetro del círculo es: {perimetro}")

#Punto 5
segundos= int(input("Por favor ingrese la cantidad de segundos: "))
horas= segundos/ 3600
print (f"{segundos} segundos equivalen a {horas} horas")

#Punto 6
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))
numero_por_0 = numero_a_multiplicar * 0
numero_por_1 = numero_a_multiplicar * 1
numero_por_2 = numero_a_multiplicar * 2
numero_por_3 = numero_a_multiplicar * 3
numero_por_4 = numero_a_multiplicar * 4
numero_por_5 = numero_a_multiplicar * 5
numero_por_6 = numero_a_multiplicar * 6
numero_por_7 = numero_a_multiplicar * 7
numero_por_8 = numero_a_multiplicar * 8
numero_por_9 = numero_a_multiplicar * 9
print(f"""
  {numero_a_multiplicar} x 0 = {numero_por_0}
  {numero_a_multiplicar} x 1 = {numero_por_1}
  {numero_a_multiplicar} x 2 = {numero_por_2}
  {numero_a_multiplicar} x 3 = {numero_por_3}
  {numero_a_multiplicar} x 4 = {numero_por_4}
  {numero_a_multiplicar} x 5 = {numero_por_5}
  {numero_a_multiplicar} x 6 = {numero_por_6}
  {numero_a_multiplicar} x 7 = {numero_por_7}
  {numero_a_multiplicar} x 8 = {numero_por_8}
  {numero_a_multiplicar} x 9 = {numero_por_9}
      """)

#Punto 7
numero1 = int(input("Por favor, ingrese un número distinto de 0: "))
numero2 = int(input("Por favor, ingrese otro número distinto de 0: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"El resultado de la suma es: {suma}")
print(f"El resultado de la resta es: {resta}")
print(f"El resultado de la multiplicación es: {multiplicacion}")
print(f"El resultado de la división es: {division}")

#Punto 8
peso = float(input("Por favor, ingrese su peso en kg: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print (f"Tu índice de masa muscular (IMC) es: {imc}")

#Punto 9
celsius = float(input("Por favor, ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print (f"La temperatura de {celsius}°C equivale a {fahrenheit}°F. ")

#Punto 10 
num1 = float(input("Por favor, ingresa el primer número: "))
num2 = float(input("Por favor, ingresa el segundo número: "))
num3 = float(input("Por favor, ingresa el tercer número: "))
promedio = (num1 + num2 + num3) / 3
print(f"El promedio de los tres números es: {promedio}")

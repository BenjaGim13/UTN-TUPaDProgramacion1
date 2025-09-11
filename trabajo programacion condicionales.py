#Punto 1

# Solicita la edad del usuario y la convierte a un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Comprueba si la edad es mayor que 18
if edad > 18:
    print("Es mayor de edad.")

#Punto 2

# Solicita la nota del usuario y la convierte a un número entero
nota = int(input("Por favor, ingresa tu nota: "))

# Comprueba si la nota es mayor o igual a 6
if nota >= 6:
    print("Aprobado.")
else:
    print("Desaprobado.")

#Punto 3

# Solicita un número al usuario y lo convierte a un número entero
numero = int(input("Por favor, ingresa un número: "))

# Comprueba si el resto de dividir el número por 2 es igual a 0
if numero % 2 == 0:
    print("Ha ingresado un número par.")
else:
    print("Por favor, ingrese un número par.")

#Punto 4

# Solicita la edad del usuario y la convierte a un número entero
edad = int(input("Por favor, ingresa tu edad: "))

# Comprueba las categorías de edad
if edad < 12:
    print("Pertenece a la categoría: Niño/a.")
elif edad >= 12 and edad < 18:
    print("Pertenece a la categoría: Adolescente.")
elif edad >= 18 and edad < 30:
    print("Pertenece a la categoría: Adulto/a joven.")
else:
    print("Pertenece a la categoría: Adulto/a.")

#Punto 5

# Solicita al usuario que ingrese una contraseña
contraseña = input("Por favor, ingrese una contraseña: ")

# Utiliza la función len() para obtener la longitud de la contraseña
longitud = len(contraseña)

# Comprueba si la longitud está entre 8 y 14 (ambos inclusive)
if longitud >= 8 and longitud <= 14:
    print("Ha ingresado una contraseña correcta.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

 #Punto 6

import random
from statistics import mean, median, mode

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeros_aleatorios)
mediana = median(numeros_aleatorios)
moda = mode(numeros_aleatorios)

print("Media:", media)
print("Mediana:", mediana)
print("Moda:", moda)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("Sin sesgo")
else:
    print("No se puede determinar el sesgo claramente")

 
 #Punto 7
 
texto = input("Ingrese una frase o palabra: ")
# Verificar el último carácter
if texto[-1].lower() in "aeiou":
    resultado = texto + "!"
else:
    resultado = texto

# Mostrar resultado
print("Resultado:", resultado)

#Punto 8
nombre = input("Por favor, ingrese su nombre: ")
print ("Seleccione una opción")
print ("1_ Si quiere su nombre en mayúsculas")
print ("2_ Si quiere su nombre en minúsculas")
print ("3_ Si quiere su nombre con la primera letra mayúscula")
opcion = input("Ingrese el número de la opción: ")

if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.capitalize())
else:
    print("Opción no válida")
    
    
#Punto 9 

terremoto = int (input("Por favor, ingrese la magnitud del terremoto: "))

if terremoto <3:
    print("Muy leve")
    
elif terremoto >= 3 and terremoto <4:
    print("Leve")
   
elif terremoto >= 4 and terremoto <5:
    print ("Moderado")
    
elif terremoto >= 5 and terremoto <6:
    print ("Fuerte")
elif terremoto >= 6 and terremoto <7:
    print ("Muy fuerte")
    
elif terremoto >7: 
    print("Extremo")
    
else:
    print ("Ingrese un valor valido")
    

#Punto 10 

hemisferio = input("Por favor, ingrese el hemisferio (N/S): ")

hemisferio = hemisferio.lower()

mes = int(input("Por favor, ingrese el mes del año en números: "))

dia = int(input("Por favor, ingrese el día del mes en números: "))

if hemisferio == "s":
  
  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Verano")

  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Otoño")
  
  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Invierno")
  
  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Primavera")

elif hemisferio == "n":

  if (mes == 12 and dia >= 21) or (mes in (1,2)) or (mes == 3 and dia <= 20):
    print("Invierno")

  elif (mes == 3 and dia >= 21) or (mes in (4,5)) or (mes == 6 and dia <= 20):
    print("Primavera")

  elif (mes == 6 and dia >= 21) or (mes in (7,8)) or (mes == 9 and dia <= 20):
    print("Verano")

  elif (mes == 9 and dia >= 21) or (mes in (10,11)) or (mes == 12 and dia <= 20):
    print("Otoño")    

           
            
    
     
     
         
                


 
 
 
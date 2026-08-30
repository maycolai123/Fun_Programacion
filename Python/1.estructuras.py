# estructuras secuenciales
print("Registro basico")
nombre = input("ingrese su nombre:")
edad = int(input("ingrese edad: "))
print(f"Nombre: {nombre} , Edad: {edad}")



# estructuras condicionales
# C simple
print("validar edad:")
if edad <18:
    print("es menor de edad")

# C doble
if edad>17:
    print("eres mayor de edad")
else: 
    print("eres menor de edad...")

# condicional multiple
opcion = int(input("ingrese un numero del 1 al 3:  "))
match opcion:
    case 1: print ("eligio la primera opcion")
    case 2: print(" eligio la segunda opcion")
    case 3: print ("eligio la tercera opcion")
    case _: print ("opcion no valiuda")
#C anidado

if opcion ==1:
    print("opcion 1")
elif opcion ==2:
    print("opcion 2")
else:
    print("opcion")

# estructuras repetitivas 

# for - para
#genera numeros del 1 al 5
for i in range(1,6):
    print(f"repeticion del numero; {i}")
    
# while - mientras
contador =1
while contador <=3:
    print(f"intento, {contador}")    
    contador+=1 # contador = a contador +1
# do while- hacer mientras
while True:
     numero = int(input("ingrese un numnero mayor a 0:"))
     if numero >0:
        break
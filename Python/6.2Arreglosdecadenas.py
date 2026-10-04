print("Arreglos de cadena")
mensaje = "fundamentos de programacion"
print(mensaje)
print(mensaje[3])
print(mensaje[10])
print(mensaje[11])

#inmutabilidad
notas=[14,20,8,15]
notas[2] =12
print(notas)

palabra = "UPN."
#palabra[3] = "♠"
print(palabra)

texto = palabra[0] + palabra[1] + palabra[2] + "♠"
print(texto)

print("conctenacion")
nombre =" pancho"
apellido = "neruda"
completo = nombre + " " + apellido
print(completo)

#longitude de cadena
cantidad = len(mensaje)
print(f'el texto{mensaje}) tiene una longitud de {cantidad} letras')
print(f'el ultimo caracter del texto es{mensaje} es {mensaje[len(mensaje)-1]}')

print("recorriendo una cadena")
for i in range(len(mensaje)):
    print(f'{i} -> {mensaje[i]}')
    
#ejercicio
"""
leer un codigo de estudiante y su carrera
formar una etiqueta
mostar la longitud codigo, carrera y etiqueta
mostar primer y ultimo caracter del codigo
recorrer ada letra de la carrera 
crear una etiqueta nueva agregando el semestre sin alterar la original
"""
"""
codigo = input("ingrese su codigo: ")
carrera = input("ingrese su carrera: ")

etiqueta = codigo + "/" + carrera
etiqueta_periodo = etiqueta + "/2026-2"

print(etiqueta)
print(f'longitud del codigo: {len(codigo)}')
print(f'longitud dela carrera: {len(carrera)}')
print(f'longitud dela etiqueta: {len(etiqueta)}')

if len(codigo) >0:
    print(f'primer caracter [codigo{0}]')
    print(f'ultimo caracter [codigo{len(codigo) -1}]')

print("recorriendo la carrera")
for i in range(len(carrera)):
    print(f'{i} -> {carrera[i]}')

print(etiqueta_periodo)    
      
#1
print("--- Resolución del Ejercicio ---")

# 1. Leer un código de estudiante y su carrera
codigo = input("Ingrese el código de estudiante: ")
carrera = input("Ingrese la carrera: ")
semestre = input("Ingrese el semestre (ej. 2026-1): ")

# 2. Formar una etiqueta
etiqueta = codigo + " - " + carrera
print(f"Etiqueta formada: {etiqueta}")

# 3. Mostrar la longitud del código, carrera y etiqueta
print(f"Longitud del código: {len(codigo)}")
print(f"Longitud de la carrera: {len(carrera)}")
print(f"Longitud de la etiqueta: {len(etiqueta)}")

# 4. Mostrar primer y último carácter del código
print(f"Primer carácter del código: {codigo[0]}")
print(f"Último carácter del código: {codigo[len(codigo) - 1]}")

# 5. Recorrer cada letra de la carrera
print("Recorriendo cada letra de la carrera:")
for i in range(len(carrera)):
    print(f"{i} -> {carrera[i]}")

# 6. Crear una etiqueta nueva agregando el semestre sin alterar la original
etiqueta_nueva = etiqueta + " - Ciclo " + semestre
print(f"Etiqueta original (sin alterar): {etiqueta}")
print(f"Etiqueta nueva con semestre: {etiqueta_nueva}")  
"""
print("metodos para trabajar con cadenas")
# find
#slicing
#split

nombre = "pancho,quizpe"
posicion_coma = nombre.find(",")

print(f'la poscion de la comna es: {posicion_coma}')


#slicing
email= "pancho.quizpe@unc.pe"
posicion_arroba= email.find("@")
usuario = email[:posicion_arroba]
dominio = email[posicion_arroba +1:]
print(f'usuario: {usuario}')
print(f'dominio: {dominio}')

#split
nombre_curso = "bigData y base de datos avanzada"
partes = nombre_curso.split(" ")
print(partes)
print(partes[0])
print(partes[1])
print(partes[2])
print(partes[3])
print(partes[4])
print(partes[5])


#replace
telefono = "+51-987-654-321"
telefono_clean = telefono.replace("-", ".")
print(f'telefono_clean: {telefono_clean}')

#upper
nombre_mayuscula = nombre.upper()
print(nombre_mayuscula)

#lower
nombre_minuscula = nombre.lower()
print(nombre_minuscula)

#strip
palabra = "     arpe  poe"
palabra_limpia = palabra.strip()

print(f'{palabra_limpia}')



































































































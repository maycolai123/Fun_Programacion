#declarar funcion
#def saludar(a,b,c): --> a,b,c son parametros
def saludar():
    print("bienvenido al curso de fundamentos de programacion")
    
    #invocar o llamar a una funcion
saludar ()
    # saludar (1,2,3) --> son argumentos

## declarar una funcion sin retorno
def menu():
    print("1. registar")
    print("2. buscar")
    print("3. salir")
    
menu()


## declarar una funcion con retorno
def producto(a,b):
    return a * b 
# llamara a la funcion con retorno pasando argumentos
resultado = producto(8,7)
print(f'{resultado}, resultado*2 = {resultado*2}')

##funcion con varios argumentos
def promedio(t1, t2, t3 , ep, ef):
    return t1*0.1 + t2*0.1 + t3*0.1 + ep*0.20 + ef*0.5

resultado = promedio(20,20,20,14,12)
print(f"tu promedio final es {resultado}")

## declarar funcion con parametros determinados
## ------------------------------------------

def saludar_estud(nombre, curso= 'fundamentos de programacion') :
    print(f'hola {nombre}, bienvenido a {curso}')
    
saludar_estud('pancho')    
saludar_estud('pancho','base de datos')

## funviones anedadas
## ------------------------------------------

def proceso_de_compra(monto):
    def aplicar_IGV(valor):
        return valor*0.18
    
    igv= aplicar_IGV(monto)
    total = monto + igv
    return total
resultado2 = proceso_de_compra(550)
print(f'total a pagar con igv es: s/{resultado2}')
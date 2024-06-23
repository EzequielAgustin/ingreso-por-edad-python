
# Paso 1: Solicitar al usuario que ingrese la edad del cliente.

edad = int(input("Por favor, ingresa tu edad: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito para ingresar a la discoteca.

permitido = True
if edad >= 18:
    permitido = True
else:
    permitido = False
    

# Paso 3: Mostrar al usuario si su cliente puede o no ingresar a la discoteca

if permitido: 
    print("Puedes ingresar al local")
else:
    print("Lo sentimos mucho, no se puede ingresar al local siendo menor de edad")

usuarios=[]

def validar_contraseña(contraseña):
    "Valida que el codigo tenga al menos 8 caracteres,1 numero,1 letra y sin espacios"

    if len(contraseña)<8:
        return False
    if ' ' in contraseña:
        return False
    
    tiene_numero=any(c.isdigit()for c in contraseña)
    tiene_letra=any(c.isalpha()for c in contraseña)

    return tiene_numero and tiene_letra

def validar_sexo(sexo):
    "Valida que el tipo de sexo esta permitido en la lista"
    sexo_valido=["m","f"]
    return sexo.lower()in sexo_valido

def nombre_existe(nombre):
    "Verifica si el nombre de usuario ya existe"
    return any(usuario['nombre'].lower() ==  nombre.lower() for usuario in usuarios)

def ingresar_usuario():
    "Ingresa un nuevo usuario"
    print("---INGRESAR NUEVO USUARIO---")

    #SOLICITA LOS DATOS
    nombre = input ("Ingrese su usuario: ")
    sexo = input("Ingrese su tipo de sexo: ")
    contraseña = input("Ingrese su contraseña: ")

    if nombre_existe(nombre):
        print("ERROR: el nombre de usuario ya existe!")
        return
    if not validar_contraseña(contraseña):
        print("ERROR: la contraseña debe tener como minimo 8 caracteres, 1 numero, 1 letra y sin espacios")
        return
    if not validar_sexo(sexo):
        print('Debe ingresar: "m","f"')
        return
    
    usuario={
        'nombre':nombre,
        'contraseña':contraseña,
        'sexo':sexo.lower(),
    }
    
    usuarios .append(usuario)
    print("Usuario ingresado con éxito!")

def buscar_usuario():
    "Funcion para buscar usuario por nombre"
    print("---BUSCAR USUARIO---")
    nombre = input("Ingrese al usuario a buscar: ")

    for usuario in usuarios:
        if usuario ['nombre'].lower() == nombre.lower():
            print(f"El usuario es: {usuario['nombre']} y su sexo es:{usuario['sexo']} ")
            return
        
        print("El usuario no se encuentra")

def eliminar_usuario():
    "Funcion para eliminar usuarios"
    print("---ELIMINAR USUARIO---")
    nombre = input("Ingrese el usuario a eliminar: ")

    for i,usuario in enumerate(usuarios):
        if usuario['nombre'].lower() == nombre.lower():
            usuarios .pop(i)
            print("Usuario eliminado: ")
            return
        
        print("El usuario no se pudo eliminar!")

def lista_usuarios():
    "Funcion para listar usuarios"
    print("---LISTA DE USUARIOS---")
    if not usuarios:
        print("No hay usuarios registrados")
        return
    for i,usuario in enumerate(usuarios,1):
            print(f"{i}. nombre: {usuario['nombre']} - sexo: {usuario['sexo']}")

def mostar_menu():
    "Muestra el menu principal"
    print("Menu principal")
    print("1.-Ingresar usuario")
    print("2.-Buscar usuario")
    print("3.-Eliminar usuario")
    print("4.-Lista de usuarios")
    print("5.-Salir")

def main():
    "Funcion principal del programa"
    while True:
        mostar_menu()
        opcion=input("Ingrese una opción: ")
        
        if opcion == "1":
            ingresar_usuario()
        elif opcion == "2":
            buscar_usuario()
        elif opcion == "3":
            eliminar_usuario()
        elif opcion == "4":
            lista_usuarios()
        elif opcion == "5":
            print("Hasta luego!")
            break
        else:
            print("Debe seleccionar una opcion valida")

if __name__=="__main__":
     main()
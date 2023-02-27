import Usuaro as usu

dicUsuarios = {}

while(true):

    print("1=Registro")
    print("2=Inicio de sesión")
    print("3=Salida")
    r = input()
    if r == 1:
        RegistroU()
    elif r == 2:
        InicioU()
    else:
        break

def RegistroU():
    ## Registro
    print("Registro")
    usuario = input("Ingresa tu usuario; ")
    password = input("Contraseña; ")
    nombre = input("Nombre; ")
    curp = input("Curp; ")
    ciudad = input("Ciudad; ")

    miUsuario = usu.Usuario(usuario,password,nombre,curp,ciudad)
    dicUsuarios += { miUsuario.curp:miUsuario }
from p8_1 import Usuario as usu
import os

def limpiar_consola():
    os.system("cls")

admin = usu("angelAdmin","1234","Angel","SARA991009HGTLCN04","NUEVO LAREDO", "Administrador")
other = usu("noAdmin","1234","No Admin","SARA991009HGTLCN05","NUEVO LAREDO")

dicUsuarios = { admin._curp:admin, 
                other._curp:other   }


def RegistroU():
    ## Registro
    print("Registro")
    usuario = input("Ingresa tu usuario; ")
    password = input("Contraseña; ")
    nombre = input("Nombre; ")
    curp = input("Curp; ")
    ciudad = input("Ciudad; ")

    if not ExisteUsuario(curp):
        miUsuario = usu(usuario,password,nombre,curp,ciudad)
        # dicUsuarios += { miUsuario._curp:miUsuario }
        dicUsuarios[miUsuario._curp] = miUsuario
    else:
        print("Este usuario ya existe\n")
        ## del(miUsuario)
        input("Press any key...")
        limpiar_consola()
        return


def ExisteUsuario(curp) -> bool:
    for key in dicUsuarios:
        if key == curp:
            # print("Este usuario ya existe")
            return True
    return False


def EsAdmin(rol) -> bool:
    if rol == "Administrador":
        return True
    else: return False


def InicioU():
    usuario = input("Ingresa tu usuario: ")
    password = input("Ingresa tu contraseña: ")

    for key in dicUsuarios:
        dicUsu = dicUsuarios[key]._usuario
        dicPass = dicUsuarios[key]._password

        if usuario == dicUsu and dicPass == password:
            
            if EsAdmin(dicUsuarios[key]._rol):
                for key2 in dicUsuarios:
                    print(dicUsuarios[key2])
                input("press any key...")
                return
            
            print(dicUsuarios[key])
            input("press any key...")
        elif usuario == dicUsu and dicPass != password:
            print("Contraseña incorrecta")


while(True):
    limpiar_consola()
    print("1=Registro")
    print("2=Inicio de sesión")
    print("3=Salida")
    r = input()
    # limpiar_consola()
    if r == "1":
        RegistroU()
    elif r == "2":
        InicioU()
    else:
        break

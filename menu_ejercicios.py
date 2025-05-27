usuario1=None
usuario2=None
usuario3=None
clave1=None
clave2=None
clave3=None




def ini():
     name=str(input("hola bienvenido inicie session con su nombre"))
     contraseña=int(input(f"ingrese su contraseña ", name))
     
     if contraseña==clave1:
        print("bienvenido al sistema")
     elif contraseña==clave2:
        print("bienvenido al sistema")
     elif contraseña==clave3:
        print("bienvenido al sistema")
     
def registrar():
    while True:
        try:
            op=int(input("***" \
            "registro" \
            "1.- user 1" \
            "2.- user 2" \
            "3.- user3 " \
            "4.- salir" \
            "             ***"))
            match op:
                case 1:
                    if usuario1==None and usuario2==None and usuario3==None:
                    print("debe tener al menos un usuario")
                    else:
                    user=input("ingrese su nombre")
                    passw=input("ingrese su contraseña")

                case 2:
                case 3:
                case 4:
                case _:



# usuario1=None
# usuario2=None
# usuario3=None
# clave1=None
# clave2=None
# clave3=None

# if usuario1==None and usuario2==None and usuario3==None:
#     print("debe tener al menos un usuario")
# else:
#     user=input("ingrese su nombre")
#     passw=input("ingrese su contraseña")
#     if (user==usuario1 and passw==clave1) or (user==usuario2 and passw==clave2) or (user==usuario3 and passw==clave3):
#          op=int(input("" \
#          "1-. iniciar sesion" \
#          "2-. registrar usuario" \
#          "3-. salir"))

    
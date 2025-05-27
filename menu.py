

while True:
    op=int(input("***" \
    "seleccione una opcion" \
    "1.- " \
    "2.-" \
    "3.-" \
    "***"))
    match op:
        case 1:
            print("1")
        case 2:
            print("2")
        case 3:
            print("saliendo")
            break
        case _:
            print("opcion invalida")
            
    
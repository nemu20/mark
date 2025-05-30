
total=0
carrito=0

def compras():
 global total,carrito

 while True:
        op=int(input('''hola bienvenido/da
                        estos son nuestros productos:
                        1.-pan.- $1000 1kg
                        2.- yogurt $250
                        3.-leche $1000 
                        4.-salir
                        '''))
        match op:
            
            case 1:
                print("pan agregado")
                total+=1000
                carrito+=1
            case 2:
                print("yogurt agregado")
                total+=+250
                carrito+=1
            case 3:
                print("yogurt agregado")
                total+=+1000
                carrito+=1
            case 4:
                print("saliendo")
                break
            case _:
                print("ingrese un producto valido o opcion")

def boleta():
  
 while True:
        
        boleta=int(input(''' desea ver boleta?
                        1.si
                        2.no(volver)
                        '''))
        match boleta:

            case 1:
                print("..........0..........")
                print(f"total de productos {carrito}")
                print("total de compras ", total)
            case 2:
                break

while True:
    interfaz=int(input("hola bienvenido al super" \
    "1.-comprar" \
    "2.-boleta"))

    match interfaz:

        case 1:
            compras()
        case 2:
            boleta()

    
    
                


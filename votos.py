
kaiser=0
borich=0
voto=0
op=0
voto=int(input("ingrese un numero de votantes"))
for i in range(voto):
    op=int(input("ingrese su voto: kaiser 1, borich 2"))
    if op==1:
        kaiser=kaiser+1
    elif op==2:
        borich=borich+1
    else:
        print("error,seleccione un voto valido")
print("los votos de kaiser son " , kaiser)
print("los votos de borich son " , borich)


if kaiser>borich:
    print("gano kaiser")
else:
    print("gano borich")



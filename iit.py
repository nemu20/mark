# dinero=0
# credito=0
# cantingresos=float(input("ingrese sus ingresos"))
# educacion=int(input("ingrese su nivel de educacion 1.basica  2.media  3.superior "))








# import random
# numero1=int(input("ingrese un numero= "))
# num2=int(input("ingrese otro numero *que sea mayor que el anterior= "))

# if num2>numero1:
#     rand=random.randint(numero1,num2)
#     for i in range (rand):
#         print("▄" )

carrito=0
total=0
descuento=0
pikachuroll=4500
otakuroll=5000
pulpovenenosoroll=5200
aguilaelectricaroll=4800

menu=int(input("hola somos sushi goku este es nuestro menu:" \
    "1-pikachu roll. $4500" \
    "2-otaku roll. $5000" \
    "3-pulpo venenoso roll. $5200" \
    "4-anguila electrica roll $4800"
    "que va a querer?"))
if menu==1:
    total+=pikachuroll+1
elif menu==2:
    total+=otakuroll+1
elif menu==3:
    total+=pulpovenenosoroll+1
elif menu==4:
     total+=aguilaelectricaroll+1
print(f"el total es {total}")    
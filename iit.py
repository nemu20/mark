# dinero=0
# credito=0
# cantingresos=float(input("ingrese sus ingresos"))
# educacion=int(input("ingrese su nivel de educacion 1.basica  2.media  3.superior "))








import random
numero1=int(input("ingrese un numero= "))
num2=int(input("ingrese otro numero *que sea mayor que el anterior= "))

if num2>numero1:
    rand=random.randint(numero1,num2)
    for i in range (rand):
        print("▄" )


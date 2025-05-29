import random
import time
conejos=0
perros_de_caza=0

numerodeperros=int(input("ingrese la cantidad de perros para cazar"))
cantmin=int(input("ingrese la cantidad minima de conejos a traer"))

conejos=random.randint(1,20)
print("ya han llegado los perros estos trajeron" )
time.sleep(1)

print(conejos)
print("conejos")
if conejos>=cantmin:
    print("genial sus perros son fascinantes merecen sus filetes")
else:
    print("mal ahi no merecen sus chuletas no cumplieron con el objetivo")

    XD=str(input("quiere sacrificarlos?"))

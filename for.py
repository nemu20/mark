# cant=int(intput("ingrese la cantidad de repeticiones "))
# for i in range(cant):
#     print("repeticion" ,i+1)


#     nombre=input("ingrese su nombre")
#     edad=input("ingrese su edad")

#     print("hola" , nombre, "su edad es", edad)
cant=int(input("ingrese la cantidad de notas"))
total=0
notasazules=0

for i in range(cant):
    print("ingrese la nota", i+1)
    nota=float(input())
    total=total+nota
    
    prom=total/cant
    
    print(f"su promedio es ()")

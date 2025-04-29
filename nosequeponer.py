edad =-1
while (edad <0 or edad >100):
    edad =int(input("ingrese edad :"))
    if (edad <0 or edad >100):
        print("error, edad fuera de rango")
print("edad ingresada exitosamente")
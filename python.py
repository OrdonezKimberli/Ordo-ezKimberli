numero=int(input("ingrese un numero entero:"))
if numero %2==0:
    print("el numero es par.")
else:
    print("el numero es impar.")
    cantidad=int(input("cunatos numeros pares desea ver?:"))
    contador=0
    i=1
    while contador<cantidad:
        if i%2==0:print("par numero"<contador+1,":",i)
        cotador+=1
        i+=1

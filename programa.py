num1=float(input("ingrese el primer numero:"))
num2=float(input("ingrese el segundo numero:"))
operacion=input("seleccione la operacion (+,-,*,/):")

if operacion=='+':
   resultado=num1+num2
     print("resultado:",resultado)
elif operacion=='-':
   resultado=num1-num2
     print("resultado:",resultado)
elif operacion=='*':
   resultado=num1*num2
     print("resultado",resultado)
elif operacion=='/':
    if num2 !=0:
   resultado=num1/num2
     print("resultado",resultado)
    else:
        print("error:no se puede dividir entre cero.")
else:
        print("operacion no valida.")

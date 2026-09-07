nombre = input("ingrese su nombre:")
cantidad = int(input("ingrese su nota:"))
suma = 0
inicio = 1
while inicio <= cantidad:
    nota = float(input(f"ingrese la nota {inicio}:"))
    if nota < 2.0 or nota > 7.0:
        print("nota valida")
    suma = suma + nota
    inicio = inicio + 1

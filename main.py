#Creando variables y ciclos en python
menuOpciones=0

while menuOpciones != 5:
    print("Bienvenido a bodegas juanFe")
    print("**********************************")

    print("1. Digita 1 para agregar productos a la bodega: ")
    print("2. Digita 2 para ver productos de la bodega: ")
    print("3. Digita 3 para calcular el costo total de la bodega: ")


    menuOpciones=int(input("\nDigita una opcion: "))

    if menuOpciones ==1 :
        print("🛒comenzaremos a registrar un producto: \n")
    elif menuOpciones ==2:
        print("👀Revisaremos nuestro inventario: \n")
    elif menuOpciones ==3:
        print("⌛Estamos calculando: \n")
    else:
        print("✖️Aun no hemos implementado esa opcion... \n")
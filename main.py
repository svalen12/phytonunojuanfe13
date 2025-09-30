#Creando variables y ciclos en python
menuOpciones=0

#pasos para crear una lista
#1. se crea una variable utilizando corchetes
listaProductos=[]

while menuOpciones != 5:
    print("Bienvenido a bodegas juanFe")
    print("**********************************")

    print("1. Digita 1 para agregar productos a la bodega: ")
    print("2. Digita 2 para ver productos de la bodega: ")
    print("3. Digita 3 para calcular el costo total de la bodega: ")


    menuOpciones=int(input("\nDigita una opcion: "))

    if menuOpciones ==1 :
        print("🛒comenzaremos a registrar un producto: \n")

        #un producto es un diccionario(objeto)
        #pasos para crear un diccionario
        #1creamos una variable utilizando llaves
        diccionarioProducto={}
        #2. Agrgamos valores y llaves al diccionario
        diccionarioProducto["id"]=int(input("Digita el nombre del producto: "))
        diccionarioProducto["nombre"]=input("Digita el nombre del producto: ")
        diccionarioProducto["descripcion"]=float(input("Digita la descripcion del producto: "))
        diccionarioProducto["precio"]=int(input("Digita el precio del producto: "))
        diccionarioProducto["cantidad"]=int(input("Digita la cantidad del producto: "))
        diccionarioProducto["imagen"]=input("Digita la imagen del producto: ")
        diccionarioProducto["marca"]=input(("Digita la marca del producto: "))

        #3. Agregamos el diccionario a la lista
        listaProductos.append(diccionarioProducto)
        print("✔️Producto agregado correctamente... \n")
    elif menuOpciones ==2:
        print("👀Revisaremos nuestro inventario: \n")
    elif menuOpciones ==3:
        print("⌛Estamos calculando: \n")
    else:
        print("✖️Aun no hemos implementado esa opcion... \n")
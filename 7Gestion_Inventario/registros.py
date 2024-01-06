import json
lista_productos = []



def agregar_producto():
    Producto_id = int(input("ingrese el codigo del producto"))
    nombre= input ("Ingrese el nombre del producto")
    valor_de_compra = float(input("ingrese el valor de compra"))
    valor_de_venta = float(input("ingrese el valor de venta"))
    stock_max = int(input("Cuantas unidades maximas son permitidas? "))
    stock_min= int(input("cuantas unidades minimas son permitidas?"))
    proveedor = input("ingrese nombre del proveedor del producto")
    lista_productos.append({'producto_id' : Producto_id, 'nombre' : nombre, 'valor_de_compra' : valor_de_compra, 'valor_de_venta' : valor_de_venta, 'stock_maximo' : stock_max, 'stock_minimo' : stock_min, 'proveedor' : proveedor })

def ver_productos():
    print("LISTA DE PRODUCTOS RESGISTRADOS")
    print(json.dumps(lista_productos, indent=2))


def actualizar_producto():
    id_prod = int(input("Digite el ID del producto a actualizar: "))
    for producto in lista_productos:
        if 'producto_id' in producto and producto['producto_id'] == id_prod:
            encontrar_producto = input("1. Actualizar stock máximo\n2. Actualizar el stock mínimo\nIngrese su elección: ")
            if encontrar_producto == "1":
                new_stock_max = int(input("Nuevo Stock Máximo: "))
                lista_productos[0]['stock_maximo'] = new_stock_max
            elif encontrar_producto == "2":
                new_stock_min = int(input("Nuevo Stock Mínimo: "))
                lista_productos[0]['stock_maximo'] = new_stock_min

def minimo_limite():
    constante = 20
    for i in lista_productos:
        for x in ['stock_minimo']:
            if i[x] <= constante :
                producto = i[x]
                nombre = i['nombre']
                print(f"los productos esta en peligro es :{nombre} con un stock de: {producto}")
            else: 
                print("no se encontro nada!")
                

def ganancia():
    for i in lista_productos:
       for n in ['nombre']: 
             for x in ['valor_de_compra']:
                for j in ['valor_de_venta']:
                    for f in ['stock_maximo']:
                        ganancia = (((i[j] - i[x])* i[f]),'del producto:',  i[n] )
                        print(json.dumps(ganancia, indent=2))






                

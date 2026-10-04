class Producto():
    def __init__(self, cod, name, prec, stock, cat):
        self.codigo = cod
        self.nombre = name
        self.precio = prec
        self.stock = stock
        self.categoria = cat

    def mostrar(self):
        print("codigo:", self.codigo,
              "\nNombre:", self.nombre,
              "\nPrecio:", self.precio,
              "\nStock:", self.stock,
              "\nCategoria:", self.categoria)


def disminuirStock(tupla):
    if listaVacia(tupla) == 1:
        print("Lista vacia")
        return
    codig = input("Indique el codigo:")
    encontr = False
    for i in tupla:
        if codig == i.codigo:
            cantidad = int(input("Cantidad:"))
            if cantidad <= i.stock:
                i.stock -= cantidad
                encontr = True
                print("Stock disminuyo:-", cantidad)
                return
            else:
                print("Cantidad mayor al stock")
    if not encontr:
        print("Codigo no encontrado")


def aumentarStock(tupla):
    if listaVacia(tupla) == 1:
        print("Lista vacia")
        return
    codig = input("Indique el codigo:")
    encontr = False
    for i in tupla:
        if codig == i.codigo:
            cantidad = float(input("indique la cantidad:"))
            i.stock += cantidad
            encontr = True
            return

    if not encontr:
        print("Codigo no encontrado")


def listaVacia(tupla):
    if len(tupla) == 0:
        return 1
    return 0


def validarCodigo(cod, tupla: tuple[Producto]):
    if listaVacia(tupla) == 1:
        return 2
    encon = False
    for i in tupla:
        if i.codigo == cod:
            encon = True
    if not encon:
        return 1
    else:
        return 0


def llenartupla(cod, tupla):
    resultado = validarCodigo(cod, tupla)
    if resultado == 0:
        return 0
    if resultado == 1 or resultado == 2:
        nom = input("NOMBRE:")
        Precio = float(input("Precio:"))
        stock = int(input("Stock:"))
        Categoria = input("Categoria:")
        prod = Producto(cod, nom, Precio, stock, Categoria)
        return prod


def mostrarDatos(tupla: tuple[Producto]):
    if listaVacia(tupla) == 1:
        print("Lista vacia")
    else:
        for i in tupla:
            i.mostrar()


def buscarProducto(tupla):
    buscar = input("Producto a buscar:")
    encon = validarCodigo(buscar, tupla)
    if encon == 2:
        print("Lista vacia")
    elif encon == 1:
        print("Producto no encontrado")
    else:
        print("Producto encontrado:", buscar)


def infoOrdenar(tupla):
    if listaVacia(tupla) == 1:
        return 0
    else:
        print("""1. Menor → mayor
2. Mayor → menor""")
        opc = int(input("ingrese una opcion"))
        return opc


def ordenamientoPrecioA(tupla1):
    tupla = list(tupla1)
    if len(tupla) == 1:
        return 1
    for i in range(len(tupla)-1):
        for j in range(len(tupla)-1-i):
            if tupla[j].precio > tupla[j+1].precio:
                tupla[j], tupla[j+1] = tupla[j+1], tupla[j]
    return tuple(tupla)


def ordenamientoPrecioD(tupla2):
    tupla = list(tupla2)
    if len(tupla) == 1:
        return 1
    for i in range(len(tupla)-1):
        for j in range(len(tupla)-1-i):
            if tupla[j].precio < tupla[j+1].precio:
                tupla[j+1], tupla[j] = tupla[j], tupla[j+1]
    return tuple(tupla)


def ordenamientoPorStockA(tupla):
    lista = list(tupla)
    if len(tupla) == 1:
        return 1
    for i in range(len(lista)-1):
        for j in range(len(tupla)-1-i):
            if lista[j].stock > lista[j+1].stock:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return tuple(lista)


def ordenamientoPorStockD(tupla):
    lista = list(tupla)
    if len(tupla) == 1:
        return 1
    for i in range(len(lista)-1):
        for j in range(len(tupla)-1-i):
            if lista[j].stock < lista[j+1].stock:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return tuple(lista)


def modificarProducto(tupla: tuple[Producto]):
    codigo = input("Ingrese el codigo:")
    validar = validarCodigo(codigo, tupla)
    if validar == 2:
        print("lista vacia")
    elif validar == 0:
        print(""""1. Modificar nombre
2. Modificar precio
3. Modificar categoría
4. Modificar stock
5. Cancelar""")
        opc = int(input("Ingrese una opcion:"))
        posicion = 0
        for indic, i in enumerate(tupla):
            if i.codigo == codigo:
                posicion = indic
        match opc:
            case 1:
                nom = input("INDIQUE EL NUEVO NOMBRE:")
                tupla[posicion].nombre = nom
            case 2:
                prec = float(input("INDIQUE EL NUEVO PRECIO:"))
                tupla[posicion].precio = prec
            case 3:
                cat = input("INDIQUE LA NUEVA CATEGORIA:")
                tupla[posicion].categoria = cat
            case 4:
                stock = int(input("INDIQUE EL NUEVO STOCK:"))
                tupla[posicion].stock = stock
            case 5:
                print("OPCION CANCELADA")
            case _:
                print("OPCION invalida")

    else:
        print("codigo no encontrado")


def eliminarProducto(tupla: tuple[Producto]):
    codigo = input("Ingrese el codigo:")
    validar = validarCodigo(codigo, tupla)
    if validar == 2:
        return 0
    elif validar == 0:
        lista = list(tupla)
        posicion = 0
        for indic, i in enumerate(tupla):
            if i.codigo == codigo:
                posicion = indic
        lista.pop(posicion)
        print("producto eliminado")
        return tuple(lista)
    else:
        return 1


def mayorPrecio(tupla3):
    May = ordenamientoPrecioD(tupla3)
    if May != 1:
        return f"{May[0].nombre} \nPrecio: {May[0].precio}"
    else:
        return 0


def menorStock(tupla4):
    Men = ordenamientoPorStockA(tupla4)
    if Men != 1:
        return f"{Men[0].nombre} \nStock: {Men[0].stock}"
    else:
        return 0


def filtrarCategoria(tupla: tuple[Producto]):
    busq = input("Ingrese la categoria a filtrar: ")
    cont = 1
    for i in tupla:
        if i.categoria == busq:
            print(
                f"{cont} |\t{i.codigo}| {i.nombre} | {i.precio} | {i.stock}| {i.categoria}")
            cont += 1


def calcInventario(tupla: tuple[Producto]):
    total = 0.0
    for i in tupla:
        total += i.precio * i.stock
    print(f"El valor total del inventario es: {total}")


tuplaProductos = tuple()
while True:
    print("""===== SISTEMA DE PRODUCTOS =====

1. Registrar producto
2. Mostrar productos
3. Buscar producto
4. Modificar producto
5. Eliminar producto
6. Aumentar stock
7. Disminuir stock
8. Ordenar por precio
9. Ordenar por stock
10. Producto con mayor precio
11. Producto con menor stock
12. Filtrar por categoría
13. Valor total del inventario
14. Salir""")
    opc = int(input("Seleccione una opcion:"))
    match opc:
        case 1:
            cod = input("Codigo:")
            resultado = llenartupla(cod, tuplaProductos)
            if resultado == 0:
                print("codigo existente")
            else:
                tuplaProductos += (resultado,)

        case 2:
            mostrarDatos(tuplaProductos)
        case 3:
            buscarProducto(tuplaProductos)
        case 4:
            modificarProducto(tuplaProductos)
        case 5:
            eliminar = eliminarProducto(tuplaProductos)
            if eliminar == 0:
                print("tupla vacia")
            elif eliminar == 1:
                print("codigo no encontrado")
            else:
                tuplaProductos = eliminar

        case 6:
            aumentarStock(tuplaProductos)
        case 7:
            disminuirStock(tuplaProductos)

        case 8:
            opc = infoOrdenar(tuplaProductos)
            if opc == 0:
                print("tupla vacia")
            else:
                match opc:
                    case 1:
                        resultadoA = ordenamientoPrecioA(tuplaProductos)
                        if resultadoA == 1:
                            print("Precio ordenado Asendente")
                        else:
                            tuplaProductos = resultadoA
                            print("Precio ordenado Asendente")
                    case 2:
                        resultadoD = ordenamientoPrecioD(tuplaProductos)
                        if resultadoD == 1:
                            print("Precio ordenado Desendentemente")
                        else:
                            tuplaProductos = resultadoD
                            print("Precio ordenado Desendentemente")
                    case _:
                        print("Opcion invalida")
        case 9:
            print()
            opc = infoOrdenar(tuplaProductos)
            if opc == 0:
                print("tupla vacia")
            else:
                match opc:
                    case 1:
                        resultadoStockA = ordenamientoPorStockA(
                            tuplaProductos)
                        if resultadoStockA == 1:
                            print("Stock ordenado Asendente")
                        else:
                            tuplaProductos = resultadoStockA
                            print("Stock ordenado Asendente")
                    case 2:
                        resultadoStockD = ordenamientoPorStockD(
                            tuplaProductos)
                        if resultadoStockD == 1:
                            print("Tupla ordenada Desendentemente")
                        else:
                            tuplaProductos = resultadoStockD
                            print("Tupla ordenada Desendentemente")
                    case _:
                        print("Opcion invalida")

        case 10:
            res = mayorPrecio(tuplaProductos)
            if res == 0:
                print("La tupla solo tiene un producto.")
            else:
                print("El producto con mayor precio es: ", res)

        case 11:
            res = menorStock(tuplaProductos)
            if res == 0:
                print("La tupla solo tiene un producto.")
            else:
                print("El producto con menor stock es: ", res)

        case 12:
            filtrarCategoria(tuplaProductos)

        case 13:
            calcInventario(tuplaProductos)

        case 14:
            print("Salinedo del programa")
            break
        case _:
            print("OPCION INVALIDA")

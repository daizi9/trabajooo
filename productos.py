def cargar_productos(nombre):
    productos=[]
    with open("nombre", "r") as archivo:
        for linea in archivo:
            linea_limpia:linea.strip()
            partes=linea_limpia.split(",")

            producto= {
                "nombre"= partes[0].strip()
                "precio"= float(partes[1].strip)
                "cantidad"= int(partes[2].strip)

            }
            productos.append(producto)
    return producto

def mostrar_produc(productos):
    for p in productos:
        print(f"Producto:{p['nombre']} | Precio:{p['precio']:.2f}" | cantidad: {p['cantidad']}")

def guardarPro(producto, nombre):
  with open(nombre, "w") as archivo:
  linea_csv = f"{p['nombre']},{p['precio']},{p['cantidad']}\n"
  archivo.write(linea_csv)
  print(f"Archivo '{nombre}' actualizado con {len(productos)} registros.")


def agregar_productos():
 nombre=input("Ingrese el nombre del nuevo producto:").strip()
 precio = float(input("Ingrese el precio: "))
 cantidad = int(input("Ingrese la cantidad: "))
 nuevo_producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }
    productos.append(nuevo_producto)
    print(f"Producto '{nombre}' agregado a la lista en memoria. Recuerde guardar los cambios.")

def buscar_prod(producto):
 nombre_buscado = input("Ingrese el nombre del producto a buscar: ").strip().lower()
 encontrado = False
    for p in productos:
        if p['nombre'].lower() == nombre_buscado:
            print("\n¡Producto Encontrado!")
            print(f"Nombre: {p['nombre']}")
            print(f"Precio: \${p['precio']:.2f}")
            print(f"Cantidad: {p['cantidad']}")
            encontrado = True
            break

#funcion principal


  








        
    
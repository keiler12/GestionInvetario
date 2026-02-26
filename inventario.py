def registrar_producto(nombre: str, cantidad: int, descripcion: str, precio: float) -> dict:
    """
    Registra un nuevo producto en el inventario.
    """
    return {
        "nombre": nombre,
        "cantidad": cantidad,
        "descripcion": descripcion,
        "precio": precio
    }
    
def actualizar_cantidad(producto: dict, cantidad: int) -> dict:
    """
    Actualiza la cantidad disponible de un producto.

    Args:
        producto (dict): El producto a actualizar.
        cantidad (int): La cantidad a sumar.

    Returns:
        dict: El producto con la cantidad actualizada.
    """
    producto["cantidad"] += cantidad
    return producto


def consultar_producto(inventario: list[dict], nombre: str) -> dict | None:
    """
    Consulta la información de un producto por nombre.

    Args:
        inventario (list[dict]): Lista de productos.
        nombre (str): Nombre del producto a buscar.

    Returns:
        dict | None: El producto encontrado o None si no existe.
    """
    return next((p for p in inventario if p["nombre"] == nombre), None)

def listar_productos(inventario: list[dict]) -> list[dict]:
    """
    Lista todos los productos registrados en el inventario.

    Args:
        inventario (list[dict]): Lista de productos.

    Returns:
        list[dict]: Copia de la lista de productos.
    """
    return inventario.copy()
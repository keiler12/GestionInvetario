#prueba para actualizar la cantidad de un producto en el inventario
from inventario import registrar_producto, actualizar_cantidad

def test_actualizar_cantidad():
    producto = registrar_producto("Laptop", 10, "Portátil", 1500.0)
    actualizar_cantidad(producto, 5)
    assert producto["cantidad"] == 15
###########################################################################


#prueba para registrar un producto en el inventario
from inventario import registrar_producto

def test_registrar_producto():
    producto = registrar_producto("Laptop", 10, "Portátil", 1500.0)
    assert producto["nombre"] == "Laptop"
    assert producto["cantidad"] == 10
    assert producto["descripcion"] == "Portátil"
    assert producto["precio"] == 1500.0                                     
#########################################################################

#prueba para consultar un producto en el inventario
from inventario import registrar_producto, consultar_producto

def test_consultar_producto():
    inventario = [
        registrar_producto("Laptop", 10, "Portátil", 1500.0),
        registrar_producto("Mouse", 50, "Inalámbrico", 25.0)
    ]
    producto = consultar_producto(inventario, "Mouse")
    assert producto is not None
    assert producto["nombre"] == "Mouse"
    assert producto["cantidad"] == 50
#################################################################
    
    
#listar los productos en el inventario
from inventario import registrar_producto, listar_productos

def test_listar_productos():
    inventario = [
        registrar_producto("Laptop", 10, "Portátil", 1500.0),
        registrar_producto("Mouse", 50, "Inalámbrico", 25.0)
    ]
    lista = listar_productos(inventario)
    assert len(lista) == 2
    assert lista[0]["nombre"] == "Laptop"
    assert lista[1]["nombre"] == "Mouse"    
    
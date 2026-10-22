from ejercicios.ejercicio1_cine import leerCantidad, calcularSubtotal, calcularDescuento, mostrarCompra
from ejercicios.ejercicio2_combustible import leerDatos, calcularRendimiento, calcularCosto, mostrarResultados


 
 
def ejecutarEjercicio1(): 
    cantidad = leerCantidad()
    subtotal = calcularSubtotal(cantidad)
    descuento = calcularDescuento(subtotal)
    mostrarCompra(cantidad, subtotal, descuento)


def ejecutarEjercicio2(): 
    datos = leerDatos()
    rendimiento = calcularRendimiento(datos)
    costo = calcularCosto(rendimiento)
    mostrarResultados(rendimiento, costo)


def mostrarMenu(): 
    print() 
    print("Menú de ejercicios") 
    print("1. Ejercicio 1: Compra de boletos de cine") 
    print("2. Ejercicio 2: Rendimiento de combustible")
    print("0. Salir")


def menus(): 
    opcion = "" 
    while opcion != "0": 
        mostrarMenu() 
        opcion = input("Seleccione una opción: ") 
        if opcion == "1": 
            ejecutarEjercicio1() 
        elif opcion == "2": 
            ejecutarEjercicio2() 
        elif opcion != "0": 

            print("Opción no válida.")
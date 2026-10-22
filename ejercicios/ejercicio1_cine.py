Un cine necesita desarrollar un programa que permita determinar el importe de una compra de boletos. 
Cada boleto cuesta $75.00. El usuario deberá indicar cuántos boletos desea comprar. Cuando se adquieran 4 
boletos o más, se aplicará un descuento del 10% sobre el subtotal. Para compras menores a 4 boletos, no se 
aplicará descuento. 
El programa deberá realizar los cálculos necesarios y presentar la siguiente información: 
• Cantidad de boletos adquiridos. 
• Precio unitario del boleto. 
• Subtotal de la compra. 
• Descuento aplicado. 
Segundo Examen Parcial · Programación Aplicada II 
• Total a pagar. 
Universidad Iberoamericana León                                           
 Ing. Alejandro Montes 
Archivo: ejercicios/ejercicio1_cine.py 
Funciones obligatorias: leerCantidad, calcularSubtotal, calcularDescuento, mostrarCompra. 
Casos de prueba (calcula manualmente los resultados esperados): 
Caso |Cantidad de boletos 
1 | 1
2 | 3
3 | 4
4 | 6

Consideraciones: la cantidad de boletos deberá ser un entero mayor que cero; los importes deberán 
mostrarse en pesos mexicanos con dos decimales y mediante tabulate.

#• PROBLEMA: Determinar el importe total de la compra de boletos de cine, considerando descuentos por cantidad.
#• ENTRADAS: cantidad de boletos (entero mayor que cero).
    #- La cantidad de boletos debe ser un entero positivo.
    #- La cantidad de boletos no debe ser cero.
    #- Los importes deben mostrarse en pesos mexicanos con dos decimales y mediante tabulate.
    #- El descuento se aplicará solo si la cantidad de boletos es mayor o igual a 4.
    #- El total a pagar debe ser un número positivo.
    #- Los importes deben mostrarse en pesos mexicanos con dos decimales y mediante tabulate.
#• SALIDAS: información que se presenta, con tipo y formato.
    #- Cantidad de boletos adquiridos (entero).
    #- Precio unitario del boleto (float con dos decimales).
    #- Subtotal de la compra (float con dos decimales).
    #- Descuento aplicado (float con dos decimales).
    #- Total a pagar (float con dos decimales).

#• REGLAS Y SUPUESTOS: valores fijos, condiciones, límites exactos y criterios de redondeo.
    #- El precio unitario del boleto es de $75.00.
    #- El descuento del 10% se aplica solo si la cantidad de boletos es mayor o igual a 4.
    #- El subtotal se calcula multiplicando la cantidad de boletos por el precio unitario.
    #- El total a pagar se obtiene restando el descuento al subtotal.
    #- Los importes deben mostrarse en pesos mexicanos con dos decimales y mediante tabulate.
    #- La cantidad de boletos debe ser un entero positivo.
    #- El total a pagar debe ser un número positivo.

#• ALGORITMO: pasos numerados y operaciones necesarias.
    #- Leer la cantidad de boletos a comprar.
    #- Calcular el subtotal multiplicando la cantidad de boletos por el precio unitario.
    #- Calcular el descuento aplicando el 10% al subtotal si la cantidad de boletos es mayor o igual a 4.
    #- Calcular el total a pagar restando el descuento al subtotal.
    #- Mostrar la información de la compra: cantidad de boletos, precio unitario, subtotal, descuento y total a pagar.

#• CASOS DE PRUEBA: entradas y resultados esperados calculados manualmente.
    # Caso 1: 2 boletos
    #   - Cantidad de boletos: 2
    #   - Precio unitario: $75.00
    #   - Subtotal: $150.00|
    #   - Descuento: $0.00
    #   - Total a pagar: $150.00
    # Caso 2: 3 boletos
    #   - Cantidad de boletos: 3
    #   - Precio unitario: $75.00
    #   - Subtotal: $225.00
    #   - Descuento: $0.00
    #   - Total a pagar: $225.00
    # Caso 3: 4 boletos
    #   - Cantidad de boletos: 4
    #   - Precio unitario: $75.00
    #   - Subtotal: $300.00
    #   - Descuento: $30.00
    #   - Total a pagar: $270.00
    # Caso 4: 6 boletos
    #   - Cantidad de boletos: 6
    #   - Precio unitario: $75.00
    #   - Subtotal: $450.00
    #   - Descuento: $45.00
    #   - Total a pagar: $405.00

#• RESTRICCIONES PARA EL AGENTE: condiciones que debe respetar Copilot; la única biblioteca externa permitida es tabulate.
    #- La cantidad de boletos debe ser un entero positivo.
    #- La cantidad de boletos no debe ser cero.
    #- Los importes deben mostrarse en pesos mexicanos con dos decimales y mediante tabulate.
    #- El descuento se aplicará solo si la cantidad de boletos es mayor o igual a 4.
    #- El total a pagar debe ser un número positivo.
    # - Implementa exactamente este algoritmo, en el mismo orden.  
    # - Usa únicamente las funciones del contrato, con esas firmas. 
    # - No agregues clases, funciones auxiliares ni bibliotecas. 
    # - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
    # - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

#• CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función. 
    #- leerCantidad: no recibe parámetros, retorna un entero mayor que cero.
    #- calcularSubtotal: recibe un entero (cantidad de boletos), retorna un float (subtotal).
    #- calcularDescuento: recibe un float (subtotal) y un entero (cantidad de boletos), retorna un float (descuento).
    #- mostrarCompra: recibe un entero (cantidad de boletos), un float (precio unitario), un float (subtotal), un float (descuento) y un float (total a pagar), no retorna nada, imprime la información de la compra.

    def leerCantidad():
        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de boletos a comprar (entero mayor que cero): "))
                if cantidad > 0:
                    return cantidad
                else:
                    print("La cantidad debe ser un entero mayor que cero. Intente nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")
                continue

    def calcularSubtotal(cantidad):
        precio_unitario = 75.00
        subtotal = cantidad * precio_unitario
        return subtotal

    def calcularDescuento(subtotal, cantidad):
        if cantidad >= 4:
            descuento = subtotal * 0.10
        else:
            descuento = 0.00
        return descuento    

    def mostrarCompra(cantidad, precio_unitario, subtotal, descuento, total):
        from tabulate import tabulate
        headers = ["Cantidad de boletos", "Precio unitario", "Subtotal", "Descuento", "Total a pagar"]
        data = [[cantidad, f"${precio_unitario:.2f}", f"${subtotal:.2f}", f"${descuento:.2f}", f"${total:.2f}"]]
        print(tabulate(data, headers=headers, tablefmt="grid"))

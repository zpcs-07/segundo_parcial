Un conductor necesita conocer el rendimiento de combustible de su vehículo y el costo de un recorrido. El 
usuario deberá proporcionar la distancia recorrida en kilómetros y la cantidad de litros consumidos. El 
precio por litro será de $24.00. 
El programa deberá realizar los cálculos necesarios y presentar la siguiente información: 
• Distancia recorrida en kilómetros. 
• Cantidad de litros consumidos. 
• Precio por litro de combustible. 
• Rendimiento del vehículo en kilómetros por litro. 
• Costo total del combustible consumido. 
Archivo: ejercicios/ejercicio2_combustible.py 
Funciones obligatorias: leerDatos, calcularRendimiento, calcularCosto, mostrarResultados. 
Casos de prueba (calcula manualmente los resultados esperados): 
Caso 
Distancia recorrida 
Litros consumidos 
1 | 120 km | 10 L
2 | 250 km | 20 L
3 | 180 km | 15 L
4 | 300 km | 25 L

Consideraciones: distancia y litros deberán ser mayores que cero. El rendimiento se mostrará con dos 
decimales; el costo, en pesos mexicanos con dos decimales. Presenta los resultados mediante tabulate.

# PROBLEMA: qué se necesita resolver, en una oración. 
    #- Calcular el rendimiento de combustible y el costo de un recorrido.
# ENTRADAS: cada dato con tipo, unidad y rango válido. 
    # - Distancia recorrida: float, km, > 0
    # - Litros consumidos: float, L, > 0
    # - Precio por litro: float, $, > 0

# SALIDAS: información que se presenta, con tipo y formato. 
    # - Distancia recorrida: float, km, > 0
    # - Litros consumidos: float, L, > 0
    # - Precio por litro de combustible: float, $, > 0
    # - Rendimiento del vehículo: float, km/L, > 0
    # - Costo total del combustible consumido: float, $, > 0

# REGLAS Y SUPUESTOS: valores fijos, condiciones, límites exactos y criterios de redondeo. 
    # - El precio por litro de combustible es de $24.00.
    # - El rendimiento se calcula como la distancia recorrida entre los litros consumidos.
    # - El costo total se calcula como los litros consumidos por el precio por litro.
    # - El rendimiento y el costo total deben ser números positivos.
    # - Los resultados deben mostrarse con dos decimales y mediante tabulate.
    # - La distancia y los litros consumidos deben ser mayores que cero.

# ALGORITMO: pasos numerados y operaciones necesarias.
    #- Leer la distancia recorrida y los litros consumidos.
    #- Calcular el rendimiento del vehículo dividiendo la distancia recorrida entre los litros consumidos
    #- Calcular el costo total del combustible consumido multiplicando los litros consumidos por el precio por litro.
    # - Mostrar los resultados utilizando tabulate.

# CASOS DE PRUEBA: entradas y resultados esperados calculados manualmente.
    #- Caso 1: 120 km, 10 L
    #   - Distancia recorrida: 120 km
    #   - Litros consumidos: 10 L
    #   - Precio por litro de combustible: $24.00
    #   - Rendimiento del vehículo: 12.00 km/L
    #   - Costo total del combustible consumido: $240.00
    #- Caso 2: 250 km, 20 L
    #   - Distancia recorrida: 250 km
    #   - Litros consumidos: 20 L
    #   - Precio por litro de combustible: $24.00
    #   - Rendimiento del vehículo: 12.50 km/L
    #   - Costo total del combustible consumido: $480.00
    #- Caso 3: 180 km, 15 L
    #   - Distancia recorrida: 180 km
    #   - Litros consumidos: 15 L
    #   - Precio por litro de combustible: $24.00
    #   - Rendimiento del vehículo: 12.00 km/L
    #   - Costo total del combustible consumido: $360.00
    #- Caso 4: 300 km, 25 L
    #   - Distancia recorrida: 300 km
    #   - Litros consumidos: 25 L
    #   - Precio por litro de combustible: $24.00
    #   - Rendimiento del vehículo: 12.00 km/L
    #   - Costo total del combustible consumido: $600.00

# RESTRICCIONES PARA EL AGENTE: condiciones que debe respetar Copilot; la única biblioteca externa permitida es tabulate.
    #- La distancia y los litros consumidos deben ser mayores que cero.
    #- El precio por litro de combustible debe ser mayor que cero.
    #- El rendimiento y el costo total deben ser números positivos.
    #- Los resultados deben mostrarse con dos decimales y mediante tabulate.
    #- La distancia y los litros consumidos deben ser mayores que cero.
    # - Implementa exactamente este algoritmo, en el mismo orden.  
    # - Usa únicamente las funciones del contrato, con esas firmas. 
    # - No agregues validaciones, mensajes ni cálculos que no estén aquí. 
    # - No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES: nombre, parámetros y valor de retorno de cada función.
    #- leerDatos: no recibe parámetros, retorna distancia (float) y litros (float)
    #- calcularRendimiento: recibe distancia (float) y litros (float), retorna rendimiento (float)
    #- calcularCosto: recibe litros (float) y precioPorLitro (float), retorna costo (float)
    #- mostrarResultados: recibe distancia (float), litros (float), precioPorLitro (float), rendimiento (float) y costo (float), no retorna valor  

    def leerDatos():
        # Leer la distancia recorrida y los litros consumidos 
        while True:
            try:
                distancia = float(input("Ingrese la distancia recorrida (km): "))
                litros = float(input("Ingrese los litros consumidos (L): "))
                if distancia > 0 and litros > 0:
                    return distancia, litros
                else:
                    print("La distancia y los litros consumidos deben ser mayores que cero.")
            except ValueError:
                print("Entrada inválida. Por favor, ingrese números válidos.")
                continue
    def calcularRendimiento(distancia, litros):
        # Calcular el rendimiento del vehículo dividiendo la distancia recorrida entre los litros consumidos
        rendimiento = distancia / litros
        return rendimiento  

    def calcularCosto(litros, precioPorLitro):
        # Calcular el costo total del combustible consumido multiplicando los litros consumidos por el precio por litro
        costo = litros * precioPorLitro
        return costo    

    def mostrarResultados(distancia, litros, precioPorLitro, rendimiento, costo):
        # Mostrar los resultados utilizando tabulate
        from tabulate import tabulate
        headers = ["Concepto", "Valor"]
        data = [
            ["Distancia recorrida (km)", f"{distancia:.2f}"],
            ["Litros consumidos (L)", f"{litros:.2f}"],
            ["Precio por litro de combustible ($)", f"{precioPorLitro:.2f}"],
            ["Rendimiento del vehículo (km/L)", f"{rendimiento:.2f}"],
            ["Costo total del combustible consumido ($)", f"{costo:.2f}"]
        ]
        print(tabulate(data, headers=headers, tablefmt="grid"))     
        
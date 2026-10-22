

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
    # - Los resultados deben mostrarse con dos decimales 
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
    #- Los resultados deben mostrarse con dos decimales
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
# - No llames a las funciones en este archivo; se llaman desde menu/menu.py.
#NO USES TABULATE

def leerDatos():
    # Leer la distancia recorrida y los litros consumidos
    distancia = float(input("Ingrese la distancia recorrida (km): "))
    litros = float(input("Ingrese los litros consumidos (L): "))
    return distancia, litros    

def calcularRendimiento(distancia, litros):
    # Calcular el rendimiento del vehículo
    rendimiento = distancia / litros
    return rendimiento

def calcularCosto(litros, precioPorLitro):
    # Calcular el costo total del combustible consumido
    costo = litros * precioPorLitro
    return costo

def mostrarResultados(distancia, litros, precioPorLitro, rendimiento, costo):
    # Mostrar los resultados
    print(f"\nDistancia recorrida: {distancia:.2f} km")
    print(f"Litros consumidos: {litros:.2f} L")
    print(f"Precio por litro de combustible: ${precioPorLitro:.2f}")
    print(f"Rendimiento del vehículo: {rendimiento:.2f} km/L")
    print(f"Costo total del combustible consumido: ${costo:.2f}\n")
   

# Se importa el modulo csv
import csv

# Nombre del archivo CSV que se va a leer (data o transacciones)
archivo = "transacciones.csv"

# Inicializamos las variables
balance = 0.0
conteo_credito = 0
conteo_debito = 0
id_max = None
monto_max = 0.0

# Se abre el archivo CSV con la funcion open, junto a sus parametros newline y encoding
with open(archivo, newline='', encoding='utf-8') as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila in lector:
        tipo = fila['tipo'].strip()
        monto = float(fila['monto'])
        id_actual = int(fila['id'])

        # Calculo del balance, diferenciando Credito y Debito
        if tipo == "Crédito":
            balance += monto
            conteo_credito += 1
        elif tipo == "Débito":
            balance -= monto
            conteo_debito += 1

        # Se identifica el ID y el monto de la transaccion mas alta
        if monto > monto_max:
            monto_max = monto
            id_max = id_actual

# Se imprime el reporte en consola
print("Reporte de Transacciones")
print("---------------------------------------------")
print(f"Balance Final: {balance:.2f}")
print(f"Transacción de Mayor Monto: ID {id_max} - {monto_max:.2f}")
print(f"Conteo de Transacciones: Crédito: {conteo_credito}  Débito: {conteo_debito}")
    

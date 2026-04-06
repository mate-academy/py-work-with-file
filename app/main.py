import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    """
    Lee transacciones de un archivo CSV, calcula el total de suministros,
    compras y el balance neto, y escribe el resultado en un nuevo CSV.
    """
    # Inicializamos los contadores
    totals = {
        "supply": 0,
        "buy": 0
    }

    # 1. Lectura y Procesamiento
    with open(data_file_name, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            # Ignoramos líneas vacías (como la última del archivo)
            if not row:
                continue

            operation_type, amount = row[0], int(row[1])
            if operation_type in totals:
                totals[operation_type] += amount

    # 2. Cálculo del Resultado
    result = totals["supply"] - totals["buy"]

    # 3. Escritura del Reporte
    with open(report_file_name, mode="w",
              encoding="utf-8", newline="") as report_file:
        writer = csv.writer(report_file)
        writer.writerow(["supply", totals["supply"]])
        writer.writerow(["buy", totals["buy"]])
        writer.writerow(["result", result])

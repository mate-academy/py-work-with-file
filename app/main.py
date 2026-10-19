import csv


def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Lendo os dados do arquivo CSV de entrada
    with open(data_file_name, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            # Ignora linhas vazias ou mal formatadas
            if not row or len(row) < 2:
                continue

            operation = row[0].strip()
            amount = int(row[1].strip())

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    # Calculando o resultado final
    result = supply_total - buy_total

    # Escrevendo o relatório no arquivo de saída
    with open(
        report_file_name,
        mode="w",
        encoding="utf-8",
        newline=""
    ) as file:
        writer = csv.writer(file)
        writer.writerow(["supply", supply_total])
        writer.writerow(["buy", buy_total])
        writer.writerow(["result", result])

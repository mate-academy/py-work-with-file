def create_report(data_file_name: str, report_file_name: str) -> str:
    supply_total = 0
    buy_total = 0

    # Lê o arquivo de entrada
    with open(data_file_name, "r") as data_file:
        lines = data_file.readlines()

        for line in lines:
            line = line.strip()

            # Ignora linhas vazias
            if not line:
                continue

            operation, amount = line.split(",")
            amount = int(amount)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    # Escreve o relatório no arquivo de saída
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")

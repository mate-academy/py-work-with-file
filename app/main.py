def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    # Lendo os dados do arquivo de entrada
    with open(data_file_name, "r") as file:
        for line in file:
            # Removendo espaços em branco e ignorando linhas vazias
            clean_line = line.strip()
            if not clean_line:
                continue

            # Separando o tipo de operação e o valor pela vírgula
            operation, amount = clean_line.split(",")
            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

    # Calculando o resultado final
    result = supply_total - buy_total

    # Escrevendo o relatório no arquivo de saída
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")

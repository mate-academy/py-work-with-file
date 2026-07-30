def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    # Ler o arquivo de entrada
    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:  # Ignorar linhas vazias
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    # Calcular o resultado
    result = total_supply - total_buy

    # Gravar no arquivo de saída
    with open(report_file_name, "w", encoding="utf-8") as f:
        f.write(f"supply,{total_supply}\n")
        f.write(f"buy,{total_buy}\n")
        f.write(f"result,{result}\n")

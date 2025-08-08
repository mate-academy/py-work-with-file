def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue  # pomiń puste linie
            operation, amount = line.split(",")
            amount = int(amount)
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f'supply,{supply_total}\n')
        file.write(f'buy,{buy_total}\n')
        file.write(f'result,{result}\n')

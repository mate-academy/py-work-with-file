def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:  # пропускаем пустые строки
                continue
            operation, amount_str = line.split(",")
            amount = int(amount_str)
            if operation == "supply":
                supply_sum += amount
            elif operation == "buy":
                buy_sum += amount

    result = supply_sum - buy_sum

    with open(report_file_name, "w", encoding="utf-8") as f:
        f.write(f"supply,{supply_sum}\n")
        f.write(f"buy,{buy_sum}\n")
        f.write(f"result,{result}\n")

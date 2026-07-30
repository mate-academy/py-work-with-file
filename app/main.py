def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as report:
        report.write(f"supply,{supply_total}\n")
        report.write(f"buy,{buy_total}\n")
        report.write(f"result,{result}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name) as data_file:
        for line in data_file:
            operation, amount = line.split(",")
            amount = int(amount)
            if not line.strip():
                continue
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount
    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")

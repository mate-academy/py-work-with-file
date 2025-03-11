def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file = open(data_file_name, "r")
    for line in data_file:
        if line.strip():
            operation, amount = line.strip().split(",")
            amount = int(amount)
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount
    data_file.close()

    result = supply_total - buy_total

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply_total}\n")
    report_file.write(f"buy,{buy_total}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()

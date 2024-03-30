def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file = open(data_file_name, "r")
    for row in data_file:
        operation, amount_str = row.split(",")
        if operation == "supply":
            supply_total += int(amount_str)
        elif operation == "buy":
            buy_total += int(amount_str)

    result = supply_total - buy_total

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply_total}\n")
    report_file.write(f"buy,{buy_total}\n")
    report_file.write(f"result,{result}\n")

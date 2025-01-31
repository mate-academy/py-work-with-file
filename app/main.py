def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(",")
                if len(parts) == 2:
                    operation, amount = parts
                    amount = int(amount)
                    if operation == "supply":
                        supply_total += amount
                    elif operation == "buy":
                        buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, "w") as report:
        report.write("supply," + str(supply_total) + "\n")
        report.write("buy," + str(buy_total) + "\n")
        report.write("result," + str(result) + "\n")
        
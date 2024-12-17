def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    with open(data_file_name, "r") as file:
        for line in file:
            if line.strip():
                operation, amount = line.strip().split(",")
                amount = int(amount)
                if operation == "supply":
                    supply_total += amount
                elif operation == "buy":
                    buy_total += amount

    result: int = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply_total) + "\n")
        report_file.write("buy," + str(buy_total) + "\n")
        report_file.write("result," + str(result) + "\n")

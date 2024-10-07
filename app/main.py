def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file = open(data_file_name, "r")
    for line in data_file:
        line = line.strip()
        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount
    result = supply_total - buy_total

    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write("supply," + str(supply_total) + "\n")
    report_file.write("buy," + str(buy_total) + "\n")
    report_file.write("result," + str(result) + "\n")

    report_file.close()

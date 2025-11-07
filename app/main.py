def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    data_file = open(data_file_name, "r", encoding="utf-8")
    for line in data_file:
        line = line.strip()
        if not line:
            continue

        operation, amount_str = line.split(",")
        amount = int(amount_str)

        if operation == "supply":
            supply_total += amount
        elif operation == "buy":
            buy_total += amount

    data_file.close()

    result = supply_total - buy_total

    report_file = open(report_file_name, "w", encoding="utf-8")
    report_file.write("supply," + str(supply_total) + "\n")
    report_file.write("buy," + str(buy_total) + "\n")
    report_file.write("result," + str(result) + "\n")
    report_file.close()

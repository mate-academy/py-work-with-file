def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    data_file = open(data_file_name, "r")
    for line in data_file:
        line = line.strip()
        if not line:
            continue
        operation, amount_str = line.split(",")
        amount = int(amount_str)

        if operation == "supply":
            supply_sum += amount
        elif operation == "buy":
            buy_sum += amount
    data_file.close()

    result = supply_sum - buy_sum
    report_file = open(report_file_name, "w")
    report_file.write("supply," + str(supply_sum) + "\n")
    report_file.write("buy," + str(buy_sum) + "\n")
    report_file.write("result," + str(result) + "\n")
    report_file.close()

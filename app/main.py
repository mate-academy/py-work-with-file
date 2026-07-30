def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name)
    supply_sum = 0
    buy_sum = 0

    for line in data:
        key, value = line.split(",")

        if key == "buy":
            buy_sum += int(value)
        if key == "supply":
            supply_sum += int(value)
    data.close()

    report = open(report_file_name, "w")
    report.write("supply" + "," + str(supply_sum) + "\n")
    report.write("buy" + "," + str(buy_sum) + "\n")
    report.write("result" + "," + str(supply_sum - buy_sum) + "\n")
    report.close()

def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_count = 0
    supply_count = 0

    data_file = open(data_file_name)

    for line in data_file:
        print(line, end="")

        if line.split(",")[0] == "buy":
            buy_count += int(line.split(",")[1])
        else:
            supply_count += int(line.split(",")[1])

    data_file.close()

    result = supply_count - buy_count

    report_file = open(report_file_name, "w")

    report_file.write("supply," + str(supply_count) + "\n")
    report_file.write("buy," + str(buy_count) + "\n")
    report_file.write("result," + str(result) + "\n")

    report_file.close()

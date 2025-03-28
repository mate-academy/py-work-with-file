def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply = 0
    buy = 0
    for data_line in data_file:
        if "supply" in data_line:
            supply += int(data_line.split(",")[1])
        if "buy" in data_line:
            buy += int(data_line.split(",")[1])

    data_file.close()

    report = [
        "supply," + str(supply) + "\n",
        "buy," + str(buy) + "\n",
        "result," + str(supply - buy) + "\n"
    ]

    report_file = open(report_file_name, "w")
    for line in report:
        report_file.write(line)

    report_file.close()

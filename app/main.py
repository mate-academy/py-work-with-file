def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    buy = 0
    supply = 0
    for line in data_file.readlines():
        data = line.split(",")
        if data[0] == "buy":
            buy += int(data[1])
        else:
            supply += int(data[1])
    report_file = open(report_file_name, "w")
    report_file.writelines(
        [
            "supply," + str(supply),
            "\nbuy," + str(buy),
            "\nresult," + str(supply - buy),
            "\n"
        ]
    )

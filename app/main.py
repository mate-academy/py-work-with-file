def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    supply = 0
    buy = 0
    file_data = open(data_file_name, "r")
    for line in file_data.readlines():
        columns = line.split(",")
        if "supply" in line:
            supply += int(columns[1])
        else:
            buy += int(columns[1])

    result = supply - buy
    file_data.close()
    new_file = open(report_file_name, "w")
    new_file.write(
        "supply," + str(supply) + "\n"
        "buy," + str(buy) + "\n"
        "result," + str(result) + "\n"
    )
    new_file.close()

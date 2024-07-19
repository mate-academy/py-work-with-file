def create_report(data_file_name: str, report_file_name: str) -> None:
    source_file = open(f"{data_file_name}", "r")
    supply = 0
    buy = 0
    for line in source_file:
        if "supply" in line:
            index_com = line.find(",") + 1
            supply += int(line[index_com:])
        if "buy" in line:
            index_com = line.find(",") + 1
            buy += int(line[index_com:])
    source_file.close()
    result = supply - buy
    report_file = open(f"{report_file_name}", "w")
    report_file.write(
        "supply," + str(supply) + "\n"
        "buy," + str(buy) + "\n"
        "result," + str(result) + "\n"
    )

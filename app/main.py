def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    supply = 0
    buy = 0
    for line in data_file:
        line = line.split(",")
        if "supply" in line:
            supply += int(line[1])

        if "buy" in line:
            buy += int(line[1])
    result = supply - buy
    data_file.close()
    report_file = open(report_file_name, "a")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")

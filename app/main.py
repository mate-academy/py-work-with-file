def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    report_file = open(report_file_name, "w")
    supply = 0
    buy = 0
    for line in data_file:
        if "supply" in line:
            supply += int(line.split(",")[1])
        elif "buy" in line:
            buy += int(line.split(",")[1])

    result = supply - buy

    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{result}\n")
    data_file.close()
    report_file.close()

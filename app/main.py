def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    file_to_reed = open(data_file_name)
    for line in file_to_reed:
        line = line.strip()
        name, value = line.split(",")
        if name == "supply":
            supply += int(value)
        elif name == "buy":
            buy += int(value)

    result = supply - buy

    report = open(report_file_name, "w")
    report.write(f"supply,{supply}\n")
    report.write(f"buy,{buy}\n")
    report.write(f"result,{result}\n")
    report.close()

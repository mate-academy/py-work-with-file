def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with open(data_file_name, "r") as data_file:
        for line in data_file.readlines():
            values = line.split(",")
            if values[0] == "supply":
                supply += int(values[1])
            if values[0] == "buy":
                buy += int(values[1])
    result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")

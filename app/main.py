def create_report(data_file_name: str, report_file_name: str) -> None:
    supply, buy = 0, 0
    with open(data_file_name, "r") as file_data:
        for line in file_data:
            line = line.replace("\n", "")
            if line.split(",")[0] == "supply":
                supply += int(line.split(",")[1])
            elif line.split(",")[0] == "buy":
                buy += int(line.split(",")[1])
            elif line == "":
                continue

    result = supply - buy
    with open(report_file_name, "a") as file_report:
        file_report.write(f"supply,{supply}\n")
        file_report.write(f"buy,{buy}\n")
        file_report.write(f"result,{result}\n")

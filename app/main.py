def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            data = line.strip().split(",")
            if len(data) < 2:
                continue
            if data[0] == "supply":
                supply += int(data[1])
            elif data[0] == "buy":
                buy += int(data[1])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")

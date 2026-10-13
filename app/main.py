def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    data = data_file.read()
    lines = data.split("\n")
    supply = 0
    buy = 0
    for line in lines:
        if line:
            parts = line.split(",")
            if parts[0] == "supply":
                supply += int(parts[1])
            elif parts[0] == "buy":
                buy += int(parts[1])
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{supply}\n")
    report_file.write(f"buy,{buy}\n")
    report_file.write(f"result,{supply - buy}\n")
    report_file.close()

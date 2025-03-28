def create_report(data_file_name: str, report_file_name: str) -> str:
    data = 0
    buy_data = 0
    with open(data_file_name, "r") as file_data:
        for line in file_data:
            line = line.split(",")
            if line[0] == "supply":
                data += int(line[1])
            else:
                buy_data += int(line[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{data}\n")
        report.write(f"buy,{buy_data}\n")
        report.write(f"result,{data - buy_data}\n")

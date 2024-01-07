def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as input_data:
        supply = 0
        buy = 0
        for line in input_data.readlines():
            splitted = line.split(",")
            if splitted[0] == "supply":
                supply += int(splitted[1])
            if splitted[0] == "buy":
                buy += int(splitted[1])
        result = supply - buy
    with open(report_file_name, "a") as report:
        report.write(f"supply, {supply}\n")
        report.write(f"buy, {buy}\n")
        report.write(f"result, {result}\n")

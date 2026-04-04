def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for line in data_file:
            current_line = line.split(",")
            if current_line[0] == "supply":
                supply += int(current_line[1])
            if current_line[0] == "buy":
                buy += int(current_line[1])
        result = supply - buy
        with open(report_file_name, "a") as report_file:
            report_file.write(f"supply,{supply}\n")
            report_file.write(f"buy,{buy}\n")
            report_file.write(f"result,{result}\n")

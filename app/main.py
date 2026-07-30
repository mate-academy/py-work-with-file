def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for data_input in data_file:
            data_input = data_input.split(",")
            if data_input[0] == "supply":
                supply += int(data_input[1])
            if data_input[0] == "buy":
                buy += int(data_input[1])
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")

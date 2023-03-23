def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as original_data:
        supply = 0
        buy = 0
        for line in original_data:
            operation, value = line.split(",")
            if operation == "buy":
                buy += int(value)
            if operation == "supply":
                supply += int(value)
        result = supply - buy
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")

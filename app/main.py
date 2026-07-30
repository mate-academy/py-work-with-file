def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as data_file:
        for line in data_file:
            line = line.strip()
            operation, value = line.split(",")
            if operation == "supply":
                supply += int(value)
            elif operation == "buy":
                buy += int(value)

    result = supply - buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")

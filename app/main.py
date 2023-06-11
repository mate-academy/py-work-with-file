def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name) as data:
        for line in data:
            operation, value = line.split(",")
            if operation == "supply":
                supply += int(value)
            else:
                buy += int(value)

    with open(report_file_name, "a") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{supply - buy}\n")

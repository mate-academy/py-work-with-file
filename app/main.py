def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_csv:
        for line in data_csv:
            operation, amount = line.split(",")
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)
    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")
    data_csv.close()
    report.close()

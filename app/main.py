def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data:
        for line in data.readlines():
            operation_type, amount = line.split(",")
            if operation_type == "supply":
                supply += int(amount)
            elif operation_type == "buy":
                buy += int(amount)
    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )

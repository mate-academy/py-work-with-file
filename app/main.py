def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as opened_file:
        for line in opened_file:
            operation_type, amount = line.strip().split(",")
            if operation_type == "supply":
                supply += int(amount)
            elif operation_type == "buy":
                buy += int(amount)

    result = supply - buy

    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")

create_report("supply.txt", "supply.txt")

from csv import reader


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data:
        supply = 0
        buy = 0

        data = reader(data)
        for line in data:
            operation, amount = line
            if len(line) != 2:
                continue
            if operation == "supply":
                supply += int(amount)
            elif operation == "buy":
                buy += int(amount)

        result = supply - buy

    with open(report_file_name, "w", newline="") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")

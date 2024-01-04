def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply = 0
        buy = 0

        for line in file.readlines():
            columns = line.strip().split(",")
            operation = columns[0]
            amount = int(columns[1])

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

        result = supply - buy

    with open(report_file_name, "a") as report:
        report.write(f"supply,{supply}\n")
        report.write(f"buy,{buy}\n")
        report.write(f"result,{result}\n")

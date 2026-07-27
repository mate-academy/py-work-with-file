def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            operation, amount = line.strip().split(",")
            amount = int(amount)

            if operation == "buy":
                buy += amount
            elif operation == "supply":
                supply += amount

    with open(report_file_name, "a") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        result = supply - buy
        report_file.write(f"result,{result}\n")

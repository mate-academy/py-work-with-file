def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_count = 0
    buy_count = 0

    with open(data_file_name, "r") as csv:
        for line in csv.readlines():
            operation, amount = line.split(",")
            if operation == "supply":
                supply_count += int(amount)
            if operation == "buy":
                buy_count += int(amount)

        result = supply_count - buy_count

    with open(report_file_name, "a") as report_file:
        report_file.write(f"supply,{supply_count}\n")
        report_file.write(f"buy,{buy_count}\n")
        report_file.write(f"result,{result}\n")

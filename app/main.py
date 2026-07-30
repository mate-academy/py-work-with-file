def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_value = 0
    buy_value = 0
    with open(data_file_name, "r") as file:
        for line in file:
            operation, amount = line.split(",")
            if operation == "supply":
                supply_value += int(amount)
            elif operation == "buy":
                buy_value += int(amount)
    result_value = supply_value - buy_value
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply_value}\n")
        report.write(f"buy,{buy_value}\n")
        report.write(f"result,{result_value}\n")

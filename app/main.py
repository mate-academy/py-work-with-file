def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_per_day = 0
    buy_per_day = 0

    with open(data_file_name, "r") as file:
        for line in file:
            operation_type, amount = line.split(",")
            if operation_type == "supply":
                supply_per_day += int(amount)
            elif operation_type == "buy":
                buy_per_day += int(amount)

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{supply_per_day}\n"
            f"buy,{buy_per_day}\n"
            f"result,{supply_per_day - buy_per_day}\n"
        )

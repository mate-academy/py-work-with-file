def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            stripped_line = line.strip()
            if not stripped_line:
                continue

            operation_type, amount = stripped_line.split(",")
            if operation_type == "supply":
                supply_total += int(amount)
            elif operation_type == "buy":
                buy_total += int(amount)

    result_total = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{result_total}\n"
        )

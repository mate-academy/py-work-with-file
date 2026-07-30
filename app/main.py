def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as file:
        for line in file:
            parts = line.split(",")

            operation_type = parts[0].strip()
            amount = int(parts[1].strip())

            if operation_type == "supply":
                supply_total += amount
            elif operation_type == "buy":
                buy_total += amount

    result = supply_total - buy_total

    with open(report_file_name, mode="w", newline="") as report_file:
        report_file.write(f"supply,{supply_total}\n")  # noqa: E231
        report_file.write(f"buy,{buy_total}\n")  # noqa: E231
        report_file.write(f"result,{result}\n")  # noqa: E231

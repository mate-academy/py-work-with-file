def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue

            operation_type, amount = line.split(",")

            if operation_type == "supply":
                supply_total += int(amount)
            elif operation_type == "buy":
                buy_total += int(amount)

    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")

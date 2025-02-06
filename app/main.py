def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name) as file:
        for line in file:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",")

            if operation == "supply":
                supply_total += int(amount)
            elif operation == "buy":
                buy_total += int(amount)

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{supply_total - buy_total}\n"
        )

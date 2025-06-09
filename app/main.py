def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            operation: str
            amount_str: str
            operation, amount_str = line.split(",")
            amount = int(amount_str)
            if operation == "supply":
                supply_total += amount
            elif operation == "buy":
                buy_total += amount

    result: int = supply_total - buy_total
    report_lines: list[str] = [
        f"supply,{supply_total}",
        f"buy,{buy_total}",
        f"result,{result}"
    ]

    with open(report_file_name, "w") as file:
        file.write("\n".join(report_lines) + "\n")

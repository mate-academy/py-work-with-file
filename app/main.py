def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0
    with open(data_file_name) as file:
        for line in file:
            line = line.strip()

            if not line:
                continue
        operation, amount = line.split(",")
        amount = int(amount)

        if operation == "supply":
            supply_total += amount
        if operation == "buy":
            buy_total += amount
    result = supply_total - buy_total
    with open(report_file_name, "w") as f:
        f.write(f"supply, {supply_total}\n")
        f.write(f"buy, {buy_total}\n)")
        f.write(f"result, {result}\n)")

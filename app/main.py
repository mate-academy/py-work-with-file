def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0
    with open(data_file_name, "r") as f:
        for line in f:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",")
            amount = int(amount)
            if operation == "buy":
                buy_total += amount
            elif operation == "supply":
                supply_total += amount

    with open(report_file_name, "a") as f:
        report = (
            f"supply,{supply_total}\n"
            f"buy,{buy_total}\n"
            f"result,{supply_total - buy_total}\n"
        )
        f.write(report)

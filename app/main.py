def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total = 0
    buy_total = 0

    with open(data_file_name, "r") as f:
        for line in f.read().splitlines():
            if not line:
                continue
            op, amount_str = line.split(",")
            amount = int(amount_str)
            if op == "supply":
                supply_total += amount
            elif op == "buy":
                buy_total += amount

    result = supply_total - buy_total
    report_lines = [
        f"supply,{supply_total}\n",
        f"buy,{buy_total}\n",
        f"result,{result}\n",
    ]

    with open(report_file_name, "w") as out:
        out.writelines(report_lines)

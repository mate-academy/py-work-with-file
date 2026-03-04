def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            amount = int(amount)
            if operation in totals:
                totals[operation] += amount

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w", encoding="utf-8") as report:
        report.write(f"supply,{totals['supply']}\n")
        report.write(f"buy,{totals['buy']}\n")
        report.write(f"result,{result}\n")
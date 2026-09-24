def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as source:
        for line in source:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            totals[operation] += int(amount)

    with open(report_file_name, "w") as report:
        report.write(
            f"supply,{totals['supply']}\n"
            f"buy,{totals['buy']}\n"
            f"result,{totals['supply'] - totals['buy']}\n"
        )

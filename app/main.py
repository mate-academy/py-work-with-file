def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue
            operation, amount = line.strip().split(",")
            totals[operation] += int(amount)
    supply, buy = totals["supply"], totals["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{supply}\n"
            f"buy,{buy}\n"
            f"result,{supply - buy}\n"
        )

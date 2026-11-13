def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(",")
            totals[operation] += int(amount)

    result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{totals['supply']}\n")
        report_file.write(f"buy,{totals['buy']}\n")
        report_file.write(f"result,{result}\n")

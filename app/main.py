def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if not line.strip():
                continue
            operation_type, amount = line.strip().split(",")
            totals[operation_type] += int(amount)
    result = totals["supply"] - totals["buy"]
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{totals['supply']}\n")
        report_file.write(f"buy,{totals['buy']}\n")
        report_file.write(f"result,{result}\n")

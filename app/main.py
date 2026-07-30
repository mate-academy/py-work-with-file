def create_report(data_file_name: str, report_file_name: str) -> str:
    with open(data_file_name, "r") as arquive:
        totals = {"supply": 0, "buy": 0}
        for line in arquive:
            if line.strip():
                parts = line.strip().split(",")
                operation = parts[0]
                amount = int(parts[1])

                totals[operation] += amount

    with open(report_file_name, "w") as report:
        report.write(f"supply,{totals['supply']}\n")
        report.write(f"buy,{totals['buy']}\n")
        report.write(f"result,{totals['supply'] - totals['buy']}\n")
    return report_file_name

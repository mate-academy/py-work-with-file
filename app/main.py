def create_report(data_file_name: str, report_file_name: str) -> None:
    report: dict = {}

    with open(data_file_name, "r") as f:
        for line in f:
            operation, amount = line.strip().split(",")
            report[operation] = report.get(operation, 0) + int(amount)

    with open(report_file_name, "w") as f:
        f.write(f"supply,{report.get('supply', 0)}\n")
        f.write(f"buy,{report.get('buy', 0)}\n")
        f.write(f"result,{report.get('supply', 0) - report.get('buy', 0)}\n")

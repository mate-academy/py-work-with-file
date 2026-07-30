def create_report(data_file_name: str, report_file_name: str = None) -> None:
    report = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            operation_type, amount = line.split(",")
            amount = int(amount)
            report[operation_type] = report.get(operation_type, 0) + amount

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in report.items():
            report_file.write(f"{key},{value}\n")

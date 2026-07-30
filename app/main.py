def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file:
        report_data = data_file.readlines()
        for report_line in report_data:
            if report_line.strip():
                operation, amount = report_line.strip().split(",")
                if operation in report:
                    report[operation] += int(amount)

    with open(report_file_name, "w") as report_file:
        report_file.write(
            f"supply,{report['supply']}\n"
            f"buy,{report['buy']}\n"
            f"result,{report['supply'] - report['buy']}\n"
        )

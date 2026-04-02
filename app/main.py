def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r") as data_file:
        report_data = data_file.readlines()
        for report_line in report_data:
            operation, amount = report_line.strip().split(",")
            report[operation] += int(amount)

    with open(report_file_name, "w") as report_file:
        report_file.write(
            "supply," + str(report["supply"]) + "\n"
            "buy," + str(report["buy"]) + "\n"
            "result," + str(report["supply"] - report["buy"]) + "\n"
        )

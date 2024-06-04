def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as file:
        for line in file:
            operation, value = line.strip().split(",")
            if operation in report:
                report[operation] += int(value)

    result = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{result}\n")

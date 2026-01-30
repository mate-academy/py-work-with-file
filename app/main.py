def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        data = data_file.readlines()
        report = {}
        for row in data:
            row = row.strip()
            key, value = row.split(",")
            report[key] = report.get(key, 0) + int(value)
    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{report['result']}\n")

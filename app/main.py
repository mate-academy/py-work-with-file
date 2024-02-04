def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as data:
        for line in data:
            if len(line) != 0:
                operation_type = line.split(",")[0]
                amount = int(line.split(",")[1])
                report_data[operation_type] += amount
    report_data["result"] = report_data["supply"] - report_data["buy"]
    with open(report_file_name, "w") as report:
        for key, value in report_data.items():
            report.write(f"{key},{value}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)
    report = {"supply": 0, "buy": 0, "result": 0}
    for line in data_file:
        report[line.split(",")[0]] += int(line.split(",")[1])
    report["result"] = report["supply"] - report["buy"]

    report_file = open(report_file_name, "w")
    for key, value in report.items():
        report_file.write(f"{key},{value}\n")

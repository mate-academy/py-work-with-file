def create_report(data_file_name: str, report_file_name: str) -> None:
    file_with_data = open(data_file_name)
    report = {"supply": 0, "buy": 0, "result": 0}
    report_str = ""
    for line in file_with_data:
        line = line.replace("\n", "").split(",")
        report[line[0]] += int(line[1])
    file_with_data.close()
    report["result"] = report["supply"] - report["buy"]
    for key, value in report.items():
        report_str = report_str + f"{key},{value}\n"
    report_file = open(report_file_name, "x")
    report_file.write(report_str)
    report_file.close()

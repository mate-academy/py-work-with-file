def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            splited_line = line.split(",")
            report[splited_line[0]] += int(splited_line[1])

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "a") as report_file:
        for operation_type, amount in report.items():
            report_file.write(operation_type + "," + str(amount) + "\n")

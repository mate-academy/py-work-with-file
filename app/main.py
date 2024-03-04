def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as data:
        for line in data.readlines():
            if line != "":
                line_list = line.split(",")
                operation_name = line_list[0]
                operation_value = int(line_list[1])
                report_data[operation_name] += operation_value

    report_data["result"] = report_data["supply"] - report_data["buy"]

    with open(report_file_name, "w") as report:
        for operation, operation_result in report_data.items():
            report.write(f"{operation},{operation_result}\n")

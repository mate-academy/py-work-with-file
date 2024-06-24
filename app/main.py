def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0, "result": 0}

    with open(data_file_name, "r") as file:
        for line in file.readlines():
            name = line.split(",")[0]
            value = int(line.split(",")[1])
            report_dict[name] += value

    report_dict["result"] = report_dict["supply"] - report_dict["buy"]

    with open(report_file_name, "w") as report:
        for operation, operation_result in report_dict.items():
            report.write("{operation},{operation_result}\n".format(
                operation=operation, operation_result=operation_result)
            )

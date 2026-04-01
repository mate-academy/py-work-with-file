def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(data_file_name) as input_data:
        data = [
            tuple([value for value in string.split(",")])
            for string in input_data.readlines()
        ]
        for operation in data:
            if operation[0] not in report:
                report[operation[0]] = int(operation[1])
            else:
                report[operation[0]] += int(operation[1])
    report["result"] = report["supply"] - report["buy"]
    with open(report_file_name, "w") as output_data:
        output_data.write(
            f"supply,{report['supply']}\nbuy,{report['buy']}\n"
            f"result,{report['result']}\n"
        )

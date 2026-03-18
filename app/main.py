def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    data_file = open(data_file_name, "r")
    for line in data_file.readlines():
        splited_line = line.rstrip("\n").split(",")
        if splited_line[0] in report:
            report[splited_line[0]] += int(splited_line[1])
        else:
            report[splited_line[0]] = int(splited_line[1])
    data_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(
        f'supply,{report["supply"]}\n'
        f'buy,{report["buy"]}\n'
        f'result,{report["supply"] - report["buy"]}\n'
    )
    report_file.close()

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_f:
        data_list = []
        for line in data_f.readlines():
            data_list.append(line.split(","))

    with open(report_file_name, "a") as report_f:
        report = {}
        for line in data_list:
            if line[0] not in report:
                report[line[0]] = int(line[1])
            else:
                report[line[0]] += int(line[1])

        report_f.write(f"supply,{report['supply']}\nbuy,{report['buy']}\n")
        report_f.write(f"result,{report['supply'] - report['buy']}\n")

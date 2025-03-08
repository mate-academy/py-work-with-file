def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    data_file = open(data_file_name)
    for line in data_file:
        report[line.split(",")[0]] = (
                report[line.split(",")[0]] + int(line.split(",")[1])
        )
    data_file.close()

    report_file = open(report_file_name, "w")
    for key in report:
        report_file.write(f"{key},{report[key]}\n")
    report_file.write(f'result,{report["supply"] - report["buy"]}\n')
    report_file.close()
def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {}
    with open(data_file_name, "r") as data:
        data_tuple = tuple(line.split(",") for line in data.read().split())
        for unit in data_tuple:
            report_dict[unit[0]] = report_dict.get(unit[0], 0) + int(unit[1])
    with open(report_file_name, "w") as report:
        report.write(f"supply,{report_dict['supply']}\n")
        report.write(f"buy,{report_dict['buy']}\n")
        report.write(f"result,{report_dict['supply'] - report_dict['buy']}\n")

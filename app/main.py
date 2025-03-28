def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name) as data_file,
        open(report_file_name, "w") as report_file
    ):
        report = {}
        for line in data_file:
            line_data = line.split(",")
            if line_data[0] not in report:
                report[line_data[0]] = int(line_data[1].strip())
            else:
                report[line_data[0]] += int(line_data[1].strip())
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{report['supply'] - report['buy']}\n")

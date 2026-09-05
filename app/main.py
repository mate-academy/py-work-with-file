def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        data = data_file.readlines()
        for line in data:
            key, value = line.split(",")
            if key not in report:
                report[key] = int(value)
            else:
                report[key] += int(value)
        print(report)
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{report['supply'] - report['buy']}\n")

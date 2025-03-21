def create_report(data_file_name: str, report_file_name: str) -> None:

    report = {}

    with open(data_file_name, "r") as data:
        for line in data.readlines():
            key, value = line.split(",")
            if key not in report:
                report[key] = int(value)
            else:
                report[key] += int(value)

    with open(report_file_name, "w") as data_report:
        result = f"supply,{report['supply']}\n" \
                 f"buy,{report['buy']}\n" \
                 f"result,{report['supply'] - report['buy']}\n"

        data_report.write(result)

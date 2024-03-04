def create_report(data_file_name: str,
                  report_file_name: str):

    data_report = {}

    with open(data_file_name, "r") as data:
        for line in data.readlines():
            subject, count = line.split(",")
            if subject not in data_report:
                data_report[subject] = int(count)
            else:
                data_report[subject] += int(count)

    with open(report_file_name, "w") as report:
        output = f"supply,{data_report['supply']}\n" \
                 f"buy,{data_report['buy']}\n" \
                 f"result,{data_report['supply'] - data_report['buy']}\n"
        report.write(output)

def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name) as file:
        report = {"supply": 0, "buy": 0}
        for line in file:
            key, value = line.split(",")
            report[key] += int(value)
        report["result"] = report["supply"] - report["buy"]

        with open(report_file_name, "w") as report_file:
            for key, value in report.items():
                report_file.write(f"{key},{value}\n")

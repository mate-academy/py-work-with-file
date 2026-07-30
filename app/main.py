def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.strip().split(",")
            report[key] += int(value)

        report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        for key, value in report.items():
            report_file.write(f"{key}" + "," + f"{value}\n")

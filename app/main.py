def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data:
        for line in data:
            key, value = line.strip().split(",")
            report_dict[key] += int(value)
    report_dict["result"] = report_dict["supply"] - report_dict["buy"]
    with open(report_file_name, "w") as report:
        for key, value in report_dict.items():
            report.write(f"{key},{value}\n")

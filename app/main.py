def create_report(data_file_name: str, report_file_name: str) -> None:
    report_dict = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as source:
        for line in source:
            key, value = line.split(",")
            report_dict[key] = report_dict.get(key) + int(value)
    report_dict["result"] = report_dict.get("supply") - report_dict.get("buy")
    with open(report_file_name, "w") as report:
        for key, value in report_dict.items():
            report.write(f"{key},{value}\n")

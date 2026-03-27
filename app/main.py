def create_report(data_file_name: str, report_file_name: str) -> None:
    data_report = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as data_file, \
            open(report_file_name, "a") as report:
        for line in data_file.readlines():
            line = line.replace("\n", "").split(",")
            data_report[line[0]] += int(line[1])
        data_report["result"] = data_report["supply"] - data_report["buy"]
        for name, number in data_report.items():
            report.write(f"{name},{number}\n")

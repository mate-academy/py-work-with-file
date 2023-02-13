def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0, "result": None}
    with open(data_file_name, "r") as source:
        for line in source.read().split("\n"):
            if line:
                report[line.split(",")[0]] += int(line.split(",")[1])

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "a") as report_file:
        for key, value in report.items():
            report_file.write(f"{key},{value}\n")

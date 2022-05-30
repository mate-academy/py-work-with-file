def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as f:
        report = {"supply": 0, "buy": 0}
        for line in f:
            key, value = line.split(",")
            report[key] += int(value)
        report["result"] = report["supply"] - report["buy"]

        with open(report_file_name, "w") as f:
            for key, value in report.items():
                f.write(f"{key},{value}\n")

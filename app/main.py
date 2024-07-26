def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            key, value = line.strip("\n").split(",")
            report[key] += int(value)

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as f:
        f.writelines(f"{key},{value}\n" for key, value in report.items())

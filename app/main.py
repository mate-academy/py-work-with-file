def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0, "result": 0}
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            report[line.split(",")[0]] += int(line.split(",")[1])

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file_out:
        for key, value in report.items():
            file_out.write(f"{key},{value}\n")

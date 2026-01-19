def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        read_content = [line.strip().split(",") for line in file.readlines()]

    report = {}
    for key, value in read_content:
        if key in report:
            report[key] += int(value)
        else:
            report[key] = int(value)
    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file_report:
        file_report.write("supply," + str(report["supply"]) + "\n")
        file_report.write("buy," + str(report["buy"]) + "\n")
        file_report.write("result," + str(report["result"]) + "\n")

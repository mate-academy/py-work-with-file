def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {}
    with open(data_file_name) as file:
        for line in file.readlines():
            key, value = line.split(",")
            report[key] = report.get(key, 0) + int(value)
        report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file:
        file.write("supply," + str(report["supply"]) + "\n")
        file.write("buy," + str(report["buy"]) + "\n")
        file.write("result," + str(report["result"]) + "\n")

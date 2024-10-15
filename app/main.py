def create_report(data_file_name: str, report_file_name: str) -> None:
    file_data = open(data_file_name, "r")
    report = {}
    for line in file_data.readlines():
        temp = line.strip().split(",")
        if temp[0] in report:
            report[temp[0]] += int(temp[1])
        else:
            report[temp[0]] = int(temp[1])
    report["result"] = report["supply"] - report["buy"]
    file_data.close()

    report_file = open(report_file_name, "a")
    report_file.write("supply")
    report_file.write(",")
    report_file.write(f"{report["supply"]}\n")

    report_file.write("buy")
    report_file.write(",")
    report_file.write(f"{report["buy"]}\n")

    report_file.write("result")
    report_file.write(",")
    report_file.write(f"{report["result"]}\n")

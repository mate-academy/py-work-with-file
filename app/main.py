def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    report = open(report_file_name, "w")
    dict_report = {"supply": 0, "buy": 0, "result": 0}
    data_file = open(data_file_name, "r", newline="")
    for line in data_file.readlines():
        line = line.strip()
        dict_report[line.split(",")[0]] += int(line.split(",")[1])
    dict_report["result"] = dict_report["supply"] - dict_report["buy"]
    {report.write(f"{key},{value}\n") for key, value in dict_report.items()}
    report.close()

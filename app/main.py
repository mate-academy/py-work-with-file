def create_report(data_file_name: str, report_file_name: str) -> None:
    data = open(data_file_name)
    report = {
        "supply": 0,
        "buy": 0,
        "result": 0
    }
    for line in data:
        line = line.rstrip("\n")
        if line == "":
            continue
        element = line.split(",")
        report[element[0]] += int(element[1])
    report["result"] = report["supply"] - report["buy"]
    new_file = open(report_file_name, "w")
    for key, value in report.items():
        new_file.write(f"{key},{value}\n")

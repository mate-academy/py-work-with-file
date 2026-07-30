def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        report = {"supply": 0, "buy": 0, "result": 0}
        for line in data_file:
            if not line:
                break

            info = line.split(",")
            if info[0] == "supply":
                report["supply"] += int(info[1])
            elif info[0] == "buy":
                report["buy"] += int(info[1])
        report["result"] = report.get("supply") - report.get("buy")

    with open(report_file_name, "w") as report_file:
        for key, value in report.items():
            report_file.write(f"{key},{value}\n")

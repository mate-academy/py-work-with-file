def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        report = {"supply": 0, "buy": 0, "result": 0}
        action = data_file.readline().split(",")
        while len(action) > 1:
            report[action[0]] += int(action[1].replace("\n", ""))
            action = data_file.readline().split(",")
        report["result"] = report["supply"] - report["buy"]
        for action, value in report.items():
            report_file.write(f"{action},{value}\n")

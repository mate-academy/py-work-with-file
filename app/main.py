def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {"supply": 0, "buy": 0}
    with (open(data_file_name, "r") as source,
          open(report_file_name, "w") as destination):
        for line in source:
            action, *numbers = line.strip().split(",")
            if action in report.keys():
                for number in numbers:
                    report[action] += int(number)
        report["result"] = report["supply"] - report["buy"]
        for name, value in report.items():
            destination.write(f"{name},{value}\n")

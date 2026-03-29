def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with (
        open(data_file_name) as file,
        open(report_file_name, "a") as report_file
    ):
        report = {"supply": 0, "buy": 0, "result": 0}

        for line in file:
            name, value = line.split(",")
            report[name] += int(value)

        report["result"] = report["supply"] - report["buy"]

        for name, value in report.items():
            report_file.write(f"{name},{value}\n")

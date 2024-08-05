def create_report(data_file_name: str, report_file_name: str) -> None:
    report_data = {"supply": 0, "buy": 0}
    with open(data_file_name, "r") as f:
        for line in f:
            if line:
                report_data[line.split(",")[0]] += int(line.split(",")[1])
        report_data["result"] = report_data["supply"] - report_data["buy"]

    with open(report_file_name, "w") as f:
        for operation, amount in report_data.items():
            f.write(f"{operation},{amount}\n")  # noqa: E231

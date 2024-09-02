def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.split(",")
            report[key] += int(value)

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply, {report["supply"]}\n".replace(" ", ""))
        report_file.write(f"buy, {report["buy"]}\n".replace(" ", ""))
        report_file.write(
            f"result, {report["supply"] - report["buy"]}\n".replace(" ", "")
        )

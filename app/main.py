def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.split(",")
            report[key] += int(value)

    supply = report["supply"]
    buy = report["buy"]
    result = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:
        report_file.write("supply," + str(supply) + "\n")
        report_file.write("buy," + str(buy) + "\n")
        report_file.write(
            "result," + str(result) + "\n")

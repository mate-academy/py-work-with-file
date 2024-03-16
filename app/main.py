def create_report(data_file_name: str, report_file_name: str) -> None:

    with open(data_file_name, "r") as data_file:

        data = data_file.read()

    data = data.split("\n")

    report = {
        "supply": 0,
        "buy": 0,
    }

    for line in data:
        if line:
            operation, amount = line.split(",")
            report[operation] += int(amount)

    report["result"] = report["supply"] - report["buy"]

    with open(report_file_name, "w") as report_file:

        for key, value in report.items():
            report_file.write(f"{key},{value}\n")

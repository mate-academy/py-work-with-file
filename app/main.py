def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        text = file.read()

    report = {
        "supply": 0,
        "buy": 0,
    }

    for line in text.splitlines():
        operation, amount = line.split(",")
        report[operation] += int(amount)

    result = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{report['supply']}\n"
            f"buy,{report['buy']}\n"
            f"result,{result}\n"
        )

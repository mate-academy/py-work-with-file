def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name)

    report: dict[str, int] = {"supply": 0, "buy": 0, "result": 0}

    for data_line in data_file:
        if data_line:
            operation, amount = data_line.split(",")
            amount = int(amount)

            report[operation] = report.get(operation, 0) + amount

    data_file.close()

    report["result"] = report["supply"] - report["buy"]

    report_file = open(report_file_name, "w")

    report_file.write(
        "\n".join(
            [
                ",".join([operation, str(amount)])
                for operation, amount in report.items()
            ]
        )
        + "\n"
    )

    report_file.close()

def create_report(data_file_name: str, report_file_name: str) -> None:
    report = {
        "supply": 0,
        "buy": 0,
    }

    with open(data_file_name, "r") as data_csv:
        for row in data_csv:
            row_data = row.split(",")
            report[row_data[0]] += int(row_data[1])

    supply = report["supply"] - report["buy"]

    with open(report_file_name, "w") as file_report:
        file_report.write((f"supply,{report['supply']}\n"
                           f"buy,{report['buy']}\n"
                           f"result,{supply}\n"))

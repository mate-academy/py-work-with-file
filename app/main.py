def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    report = {"supply": 0, "buy": 0}
    market_data = open(data_file_name, "r")
    for line in market_data.readlines():
        operation_type, amount = line.split(",")
        report[operation_type] += int(amount)
    market_data.close()

    report_file = open(report_file_name, "w")
    report_file.write(
        f"supply,{report['supply']}\n"
        f"buy,{report['buy']}\n"
        f"result,{report['supply'] - report['buy']}\n"
    )
    report_file.close()

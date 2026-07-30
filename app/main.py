def create_report(
    data_file_name: str,
    report_file_name: str,
) -> None:
    report = {
        "supply": 0,
        "buy": 0,
    }
    for line in open(data_file_name):
        line = line.split(",")
        operation_type = line[0]
        amount = int(line[1][:-1])
        report[operation_type] += amount
    report["result"] = report["supply"] - report["buy"]

    open(report_file_name, "w").write(
        f"supply,{report['supply']}\n"
        f"buy,{report['buy']}\n"
        f"result,{report['result']}\n"
    )

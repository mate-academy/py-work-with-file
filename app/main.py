def parse_csv(data: str) -> tuple[tuple]:
    return tuple(
        tuple(line.split(","))
        for line in data.split("\n")[:-1]
    )


def summarize_report(data: tuple[tuple]) -> dict:
    report = {operation: 0 for operation, _ in data}
    for operation, count in data:
        report[operation] += int(count)
    report["result"] = report["supply"] - report["buy"]
    return report


def create_report(
    data_file_name: str,
    report_file_name: str
) -> None:
    with open(data_file_name, "r") as data_file:
        data = parse_csv(data_file.read())
        report = summarize_report(data)
        data_file.close()

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{report['result']}\n")

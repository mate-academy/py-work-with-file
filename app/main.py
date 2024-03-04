def create_report(data_file_name: str, report_file_name: str) -> None:
    d = {}
    with open(data_file_name, "r") as source:
        for line in source.readlines():
            operation, value = line.split(",")
            d[operation] = d.get(operation, 0) + int(value)

    with open(report_file_name, "x") as report:
        report.write(f"supply,{d['supply']}\n")
        report.write(f"buy,{d['buy']}\n")
        report.write(f"result,{d['supply'] - d['buy']}\n")

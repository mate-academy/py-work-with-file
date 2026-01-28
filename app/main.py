def create_report(data_file_name: str, report_file_name: str) -> None:

    report = {}

    data_file = open(data_file_name)

    for line in data_file:
        if line:
            item, qty = line.split(",")
            report[item] = report.get(item, 0) + int(qty)

    data_file.close()

    report_file = open(report_file_name, "w")

    report_file.write(f'supply,{report.get("supply", 0)}\n')
    report_file.write(f'buy,{report.get("buy", 0)}\n')
    report_file.write(f"result,"
                      f'{(report.get("supply", 0)
                          - report.get("buy", 0))}\n')
    report_file.close()

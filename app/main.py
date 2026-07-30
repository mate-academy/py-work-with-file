def create_report(data_file_name: str, report_file_name: str) -> None:
    report_content = {}
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            key, value = line.strip().split(",")
            report_content[key] = report_content.get(key, 0) + int(value)

    supply_total = report_content.get("supply", 0)
    buy_total = report_content.get("buy", 0)
    result = supply_total - buy_total

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    supply_sum = 0
    buy_sum = 0
    for line in data_file:
        parts = line.strip().split(",")
        if not parts or not parts[0]:
            continue
        operation = parts[0]
        amount = int(parts[1])
        if operation == "supply":
            supply_sum += amount
        else:
            buy_sum += amount
    data_file.close()
    with open(report_file_name, "w") as report:
        report.write(f"supply,{supply_sum}\n")
        report.write(f"buy,{buy_sum}\n")
        report.write(f"result,{supply_sum - buy_sum}\n")

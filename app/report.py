def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_total: int = 0
    buy_total: int = 0

    with open(data_file_name, 'r') as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            operation, amount = line.split(',')
            if operation == 'supply':
                supply_total += int(amount)
            elif operation == 'buy':
                buy_total += int(amount)

    result: int = supply_total - buy_total

    with open(report_file_name, 'w') as report_file:
        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{result}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    totals = {'supply': 0, 'buy': 0}

    with open(data_file_name, 'r', encoding='utf-8') as data_file:
        for line in data_file:
            clear_line = line.strip()
            if not clear_line:
                continue
            operation, amount = clear_line.split(',')
            totals[operation] += int(amount)

    supply_count = totals['supply']
    buy_count = totals['buy']
    result = supply_count - buy_count

    with open(report_file_name, 'w', encoding='utf-8') as report_file:
        report_file.write(f'supply,{supply_count}\n')
        report_file.write(f'buy,{buy_count}\n')
        report_file.write(f'result,{result}\n')

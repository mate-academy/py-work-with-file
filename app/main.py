def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if line == '':
                continue

            parts = line.split(',')
            if len(parts) != 2:
                continue

            operation = parts[0].strip()
            try:
                amount = int(parts[1].strip())
            except ValueError:
                continue

            if operation == 'supply':
                total_supply += amount
            elif operation == 'buy':
                total_buy += amount

    result = total_supply - total_buy
    lines = [
        f"supply,{total_supply}",
        f"buy,{total_buy}",
        f"result,{result}"
    ]
    with open(report_file_name, 'w') as out:
        out.write('\n'.join(lines) + '\n')

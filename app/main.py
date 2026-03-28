def create_report(data_file_name: str, report_file_name: str) -> None:

    supply = 0
    buy = 0

    with open(data_file_name, 'r') as infile:
        for line in infile:
            parts1 = line.strip()
            if not parts1:
                continue
            parts2 = parts1.split(',')
            if len(parts2) != 2:
                continue
            op = parts2[0].strip()
            amt = parts2[1].strip()
            try:
                value = int(amt)
            except ValueError:
                continue

            if op == 'supply':
                supply += value

            elif op == 'buy':
                buy += value

    with open(report_file_name, 'w', encoding='utf-8') as f:
        f.write(f'supply,{supply}\n')
        f.write(f'buy,{buy}\n')
        f.write(f'result,{supply - buy}\n')

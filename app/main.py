def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(',')
            if len(parts) < 2:
                continue
            op = parts[0].strip()
            amt = int(parts[1].strip())
            if op == 'supply':
                total_supply += amt
            elif op == 'buy':
                total_buy += amt

    with open(report_file_name, 'w') as out:
        out.write(f"supply,{total_supply}\n")
        out.write(f"buy,{total_buy}\n")
        out.write(f"result,{total_supply - total_buy}\n")
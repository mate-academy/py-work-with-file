def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", encoding="utf-8") as f:
        totals = {"supply": 0, "buy": 0}
        for line in f:
            line = line.strip()
            if not line:
                continue
            op, amount_str = line.split(",", 1)
            op = op.lower()
            op = op.strip()
            amount = int(amount_str.strip())
            if op in totals:
                totals[op] += amount
        result = totals["supply"] - totals["buy"]

    with open(report_file_name, "w", encoding="utf-8") as f:
        f.write(f'supply,{totals["supply"]}\n')
        f.write(f'buy,{totals["buy"]}\n')
        f.write(f'result,{result}\n')

from typing import Dict


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals: Dict[str, int] = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", encoding="utf-8") as fin:
        for raw_line in fin:
            line = raw_line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                continue
            op = parts[0].strip()
            amount_str = parts[1].strip()
            try:
                amount = int(amount_str)
            except ValueError:
                try:
                    amount = int(float(amount_str))
                except Exception:
                    continue

            if op in totals:
                totals[op] += amount
            else:
                continue

    supply_total = totals["supply"]
    buy_total = totals["buy"]
    result = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as fout:
        fout.write(f"supply,{supply_total}\n")
        fout.write(f"buy,{buy_total}\n")
        fout.write(f"result,{result}\n")

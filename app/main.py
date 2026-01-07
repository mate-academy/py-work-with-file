from typing import Dict


def create_report(data_file_name: str, report_file_name: str) -> None:
    totals: Dict[str, int] = {
        "supply": 0,
        "buy": 0
    }

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            operation, amount = line.split(",")
            amount = int(amount)

            if operation in totals:
                totals[operation] += amount

    supply_total: int = totals["supply"]
    buy_total: int = totals["buy"]
    result: int = supply_total - buy_total

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{supply_total}\n")
        file.write(f"buy,{buy_total}\n")
        file.write(f"result,{result}\n")

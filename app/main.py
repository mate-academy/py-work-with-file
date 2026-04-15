import os
from typing import Dict


def create_report(data_file_name: str, report_file_name: str) -> None:
    base_dir: str = os.path.dirname(os.path.dirname(__file__))
    data_path: str = os.path.join(base_dir, data_file_name)

    report: Dict[str, int] = {
        "supply": 0,
        "buy": 0,
    }

    with (
        open(data_path, "r", encoding="utf-8") as data_file,
        open(report_file_name, "w", encoding="utf-8") as report_file,
    ):
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            operation, amount_str = line.split(",")
            amount: int = int(amount_str)

            report[operation] += amount

        result: int = report["supply"] - report["buy"]

        report_file.write(f"supply,{report['supply']}\n")
        report_file.write(f"buy,{report['buy']}\n")
        report_file.write(f"result,{result}\n")

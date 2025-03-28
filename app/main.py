import csv
import os
from typing import Dict, Optional, Type
from types import TracebackType


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(
            self,
            exc_type: Optional[Type[BaseException]],
            exc_val: Optional[BaseException],
            exc_tb: Optional[TracebackType],
    ) -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)


def create_report(data_file_name: str, report_file_name: str) -> None:

    operations: Dict[str, int] = {"supply": 0, "buy": 0}

    with open(data_file_name, "r", newline="") as infile:
        reader = csv.reader(infile)
        for row in reader:
            if row:
                try:
                    operation_type, amount_str = row
                    amount = int(amount_str)
                    operations[operation_type] += amount
                except (ValueError, KeyError):
                    continue

    result = operations["supply"] - operations["buy"]

    with open(report_file_name, "w", newline="") as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["supply", operations["supply"]])
        writer.writerow(["buy", operations["buy"]])
        writer.writerow(["result", result])

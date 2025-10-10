from typing import TextIO


def create_report(data_file_name: str, report_file_name: str) -> None:
    """Зчитує CSV-файл із операціями supply/buy та створює звіт."""
    total_supply: int = 0
    total_buy: int = 0

    with open(data_file_name, encoding="utf-8") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            operation, amount_str = line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result: int = total_supply - total_buy
    report_lines: list[str] = [
        f"supply,{total_supply}",
        f"buy,{total_buy}",
        f"result,{result}",
    ]

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write("\n".join(report_lines))

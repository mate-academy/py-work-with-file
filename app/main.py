from pathlib import Path


def create_report(data_file_name: str, report_file_name: str) -> None:
    try:
        lines = Path(data_file_name).read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        lines = (Path(__file__).parent.parent / data_file_name)\
            .read_text(encoding="utf-8").splitlines()

    supply_total = 0
    buy_total = 0

    for line in lines:
        if not line:
            continue

        operation, amount_str = line.split(",", 1)
        quantity = int(amount_str)
        if operation == "supply":
            supply_total += quantity
        else:
            buy_total += quantity

    report_text = (
        f"supply,{supply_total}\n"
        f"buy,{buy_total}\n"
        f"result,{supply_total - buy_total}\n"
    )

    Path(report_file_name).write_text(report_text, encoding="utf-8")

def create_report(
        data_file_name: str,
        report_file_name: str
) -> None:
    operations_totals: dict[str, int] = {}

    with open(data_file_name, "r", encoding="utf-8") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            key, number_str = line.split(",")
            number = int(number_str)
            operations_totals[key] = operations_totals.get(key, 0) + number

    total_supply = operations_totals.get("supply", 0)
    total_buy = operations_totals.get("buy", 0)
    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

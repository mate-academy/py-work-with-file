def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply: int = 0
    total_buy: int = 0

    with open(data_file_name, "r", encoding="utf-8") as data_file:
        for line in data_file:
            line = line.strip()

            if not line:
                continue

            operation_type, amount_str = line.split(",")
            amount: int = int(amount_str)

            if operation_type == "supply":
                total_supply += amount
            elif operation_type == "buy":
                total_buy += amount

    result: int = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

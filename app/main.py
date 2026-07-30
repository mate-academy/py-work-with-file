def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file_in:
        for line in file_in:
            clean_line = line.strip()

            if not clean_line:
                continue

            operation, amount_str = clean_line.split(",")
            amount = int(amount_str)

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as file_out:
        file_out.write(f"supply,{total_supply}\n")
        file_out.write(f"buy,{total_buy}\n")
        file_out.write(f"result,{result}\n")

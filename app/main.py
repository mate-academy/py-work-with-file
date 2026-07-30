def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file_in:
        for line in file_in:
            if not line.strip():
                continue

            operation, amount = line.strip().split(",")
            if operation == "supply":
                total_supply += int(amount)
            elif operation == "buy":
                total_buy += int(amount)

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as file_out:
        file_out.write(f"supply,{total_supply}\n")
        file_out.write(f"buy,{total_buy}\n")
        file_out.write(f"result,{result}\n")

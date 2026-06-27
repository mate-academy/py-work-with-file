def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            parts = line.split(",")
            operation = parts[0].strip()
            amount = int(parts[1].strip())

            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount

    result = total_supply - total_buy

    with open(report_file_name, "w", encoding="utf-8") as file:
        file.write(f"supply,{total_supply}\n")
        file.write(f"buy,{total_buy}\n")
        file.write(f"result,{result}\n")

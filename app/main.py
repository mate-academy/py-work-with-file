def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", encoding="utf-8") as file:
        total_supply = 0
        total_buy = 0
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError("Invalid line")
            operation = parts[0]
            amount = int(parts[1])
            if operation == "supply":
                total_supply += amount
            elif operation == "buy":
                total_buy += amount
            else:
                pass
        result = total_supply - total_buy
    with open(report_file_name, "w", encoding="utf-8") as out:
        out.write(f"supply,{total_supply}\n")
        out.write(f"buy,{total_buy}\n")
        out.write(f"result,{result}\n")

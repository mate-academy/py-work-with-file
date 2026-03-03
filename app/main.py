def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 2:
                continue

            operation, amount_str = parts

            try:
                amount = int(amount_str)
            except ValueError:
                continue

            if operation == "supply":
                supply += amount
            elif operation == "buy":
                buy += amount

    result = supply - buy

    with open(report_file_name, "w", encoding="utf-8") as out:
        out.write(f"supply,{supply}\n")
        out.write(f"buy,{buy}\n")
        out.write(f"result,{result}\n")

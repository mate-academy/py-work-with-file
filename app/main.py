def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) < 2:
                continue
            try:
                amount = int(parts[1])
            except ValueError:
                continue
            if parts[0] == "buy":
                total_buy += amount
            elif parts[0] == "supply":
                total_supply += amount
    result = total_supply - total_buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

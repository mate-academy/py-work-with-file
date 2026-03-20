def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r", encoding="utf-8") as data_file,
          open(report_file_name, "w", encoding="utf-8") as report_file):
        total_supply = 0
        total_buy = 0
        for line in data_file:
            parts = line.strip().split(",")
            if len(parts) < 2:
                continue
            if parts[0] == "supply":
                total_supply += int(parts[1])

            elif parts[0] == "buy":
                total_buy += int(parts[1])

        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{total_supply - total_buy}\n")

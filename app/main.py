def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_total = 0
    supply_total = 0
    with open(data_file_name) as data_file:
        for line in data_file:
            if not line.strip():
                continue

            parts = line.strip().split(",")

            if parts[0] == "supply":
                supply_total += int(parts[1])
            elif parts[0] == "buy":
                buy_total += int(parts[1])

    with open(report_file_name, "w") as report_file:

        report_file.write(f"supply,{supply_total}\n")
        report_file.write(f"buy,{buy_total}\n")
        report_file.write(f"result,{supply_total - buy_total}\n")

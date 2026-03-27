def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    data = open(data_file_name, "r")

    for item in data:
        parts = item.split(",")

        if "supply" in item:
            supply = int(parts[1].strip())
            total_supply += supply

        if "buy" in item:
            buy = int(parts[1].strip())
            total_buy += buy

    result = total_supply - total_buy

    data.close()

    report = open(report_file_name, "w")

    report.write(f"supply,{total_supply}\n")
    report.write(f"buy,{total_buy}\n")
    report.write(f"result,{result}\n")

    report.close()

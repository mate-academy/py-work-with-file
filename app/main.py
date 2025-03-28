def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name) as current_data:
        for line in current_data:
            name, value = line.split(",")
            if name == "supply":
                total_supply += int(value)
            elif name == "buy":
                total_buy += int(value)

    with open(report_file_name, "wt") as upgraded_report:
        upgraded_report.write(
            f"supply,{total_supply}\n"
            f"buy,{total_buy}\n"
            f"result,{total_supply - total_buy}\n"
        )

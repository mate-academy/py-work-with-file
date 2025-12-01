def create_report(data_file_name: str,
                  report_file_name: str,) -> None:
    total_supply = 0
    total_buy = 0
    new_file = open(data_file_name, "r")
    for i in new_file:
        part = i.split(",")

        if "supply" in i:
            supply = int(part[1].strip())
            total_supply += supply

        if "buy" in i:
            buy = int(part[1].strip())
            total_buy += buy

    result = total_supply - total_buy

    new_file.close()

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{total_supply}\n")
    report_file.write(f"buy,{total_buy}\n")
    report_file.write(f"result,{result}\n")

    report_file.close()

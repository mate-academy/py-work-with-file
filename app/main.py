def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if parts[0] == "supply":
                total_supply += int(parts[1])
            elif parts[0] == "buy":
                total_buy += int(parts[1])

    result = total_supply - total_buy

    write_to_file = open(report_file_name, "a")
    write_to_file.write(
        f"supply,{total_supply}\n"
        f"buy,{total_buy}\n"
        f"result,{result}\n"
    )

    write_to_file.close()

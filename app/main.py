def create_report(create_report: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(create_report, "r") as file:
        for line in file:
            clean_line = line.strip()
            if not clean_line:
                continue
            clean_line = clean_line.split(",")
            action = clean_line[0]
            amount = clean_line[1]
            if action == "supply":
                total_supply += int(amount)
            elif action == "buy":
                total_buy += int(amount)

    result = total_supply - total_buy

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{total_supply}\n"
            f"buy,{total_buy}\n"
            f"result,{result}\n"
        )

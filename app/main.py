def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue

            action, amount = line.split(",")
            amount = int(amount)

            if action == "supply":
                total_supply += amount
            if action == "buy":
                total_buy += amount

        data_file.close()

    result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")
        report_file.close()

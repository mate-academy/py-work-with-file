def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip()
            if not line:
                continue
            name, value = line.split(",")
            value = int(value)

            if name == "supply":
                total_supply += value
            elif name == "buy":
                total_buy += value

        result = total_supply - total_buy

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

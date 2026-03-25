def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy = 0
    total_supply = 0
    result = 0
    with open(data_file_name, "r") as f:
        for line in f:
            typ, value = line.strip().split(",")
            value = int(value)

            if typ == "buy":
                total_buy += value
            if typ == "supply":
                total_supply += value

        result += total_supply - total_buy

    with open(report_file_name, "w") as f:
        f.write(f"supply,{total_supply}\n")
        f.write(f"buy,{total_buy}\n")
        f.write(f"result,{result}\n")

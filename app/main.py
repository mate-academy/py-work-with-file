def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as f:
        total_supply = 0
        total_buy = 0
        for line in f:
            index, value = line.split(",")
            if index == "supply":
                total_supply += int(value)
            if index == "buy":
                total_buy += int(value)
        result = total_supply - total_buy

        with open(report_file_name, "a") as r:
            r.write(f"supply,{total_supply}\n")
            r.write(f"buy,{total_buy}\n")
            r.write(f"result,{result}\n")

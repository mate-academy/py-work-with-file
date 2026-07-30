def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            line_list = line.strip().split(",")
            if len(line_list) != 2:
                continue

            if line_list[0] == "supply":
                total_supply += int(line_list[1])
            elif line_list[0] == "buy":
                total_buy += int(line_list[1])

        result = total_supply - total_buy

    with open(report_file_name, "w", newline="") as r:
        r.write(f"supply,{total_supply}\n")
        r.write(f"buy,{total_buy}\n")
        r.write(f"result,{result}\n")

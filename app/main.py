def create_report(data_file_name: str, report_file_name: str) -> None:
    total_buy, total_supply = 0, 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            line = line.strip().split(",")
            if line:
                if line[0] == "buy":
                    total_buy += int(line[1])
                elif line[0] == "supply":
                    total_supply += int(line[1])
    with open(report_file_name, "w") as result_file:
        result_file.write(f"supply,{total_supply}\n")
        result_file.write(f"buy,{total_buy}\n")
        result_file.write(f"result,{total_supply - total_buy}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input:
        total_supply = 0
        total_buy = 0
        for line in input:
            if line == "":
                continue
            if "supply" in line:
                total_supply += int(line[7:])
            elif "buy" in line:
                total_buy += int(line[4:])
        result = total_supply - total_buy
    with open(report_file_name, "w") as output:
        output.write(f"supply,{total_supply}\n")
        output.write(f"buy,{total_buy}\n")
        output.write(f"result,{result}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        total_supply = 0
        total_buy = 0
        for line in file:
            line = line.split(",")
            clean_line = int(line[1].strip("\n"))
            if line[0] == "supply":
                total_supply += clean_line
            if line[0] == "buy":
                total_buy += clean_line
    result = total_supply - total_buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

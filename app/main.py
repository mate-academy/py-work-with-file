

def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    data = open(data_file_name)
    for line in data.readlines():
        split_line = line.split(",")
        if "supply" in split_line:
            total_supply += int(split_line[1])
        if "buy" in split_line:
            total_buy += int(split_line[1])
    data.close()

    result = total_supply - total_buy

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{total_supply}\n")
    report_file.write(f"buy,{total_buy}\n")
    report_file.write(f"result,{result}\n")
    report_file.close()

def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r") as file_in:
        for line in file_in:
            items = line.split(",")
            if items[0] == "supply":
                total_supply += int(items[1])
            if items[0] == "buy":
                total_buy += int(items[1])
        result = total_supply - total_buy
        with open(report_file_name, "w") as file_out:
            file_out.writelines(f"supply,{total_supply}\n")
            file_out.writelines(f"buy,{total_buy}\n")
            file_out.writelines(f"result,{result}\n")

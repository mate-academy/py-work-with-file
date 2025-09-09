def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0
    with open(data_file_name, "r" ) as old_file :
        for line in old_file :
            if not line.strip():
                continue
            if "supply" in line :
                total_supply += int(line.strip().split(",")[1])
            if "buy" in line :
                total_buy += int(line.split(",")[1])
        with open(report_file_name, "w") as new_file :
            new_file.write(f"supply,{total_supply}\n"
                           f"buy,{total_buy}\n"
                           f"result,{total_supply - total_buy}\n")




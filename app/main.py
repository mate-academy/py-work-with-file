def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as csvfile,\
            open(report_file_name, "w") as csvfile_1:
        all_supply = []
        all_buy = []
        for line in csvfile:
            line_list = line.split(",")
            if line_list[0] == "supply":
                all_supply.append(int(line_list[1]))
            elif line_list[0] == "buy":
                all_buy.append(int(line_list[1]))
        result = sum(all_supply) - sum(all_buy)

        csvfile_1.write(f"supply,{sum(all_supply)}\n")
        csvfile_1.write(f"buy,{sum(all_buy)}\n")
        csvfile_1.write(f"result,{result}\n")

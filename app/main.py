def create_report(data_file_name: str, report_file_name: str) -> None:
    sum_buy_supply = {"supply": 0, "buy": 0}
    file_for_read = open(data_file_name, "r")
    for line in file_for_read:
        if not line:
            continue
        split_file = line.strip().split(",")
        if split_file[0] == "supply":
            sum_buy_supply["supply"] += int(split_file[1])
        if split_file[0] == "buy":
            sum_buy_supply["buy"] += int(split_file[1])
    file_for_read.close()

    supply = sum_buy_supply["supply"]
    buy = sum_buy_supply["buy"]
    result = supply - buy

    file_for_write = open(report_file_name, "w")
    file_for_write.write(f"supply,{supply}\n")
    file_for_write.write(f"buy,{buy}\n")
    file_for_write.write(f"result,"
                         f"{result}\n")
    file_for_write.close()

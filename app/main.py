def create_report(data_file_name: str, report_file_name: str) -> None:
    data_file = open(data_file_name, "r")
    buy_supply = {"supply": 0, "buy": 0}
    for line in data_file.readlines():
        line_list = line.split(",")
        if len(line_list) == 2:
            if "supply" in line_list:
                buy_supply["supply"] += int(line_list[1])
            elif "buy" in line_list:
                buy_supply["buy"] += int(line_list[1])
    result = buy_supply["supply"] - buy_supply["buy"]
    new_file = open(report_file_name, "a")
    supply = "supply," + str(buy_supply["supply"]) + "\n"
    new_file.write(supply)
    buy = "buy," + str(buy_supply["buy"]) + "\n"
    new_file.write(buy)
    result_str = "result," + str(result) + "\n"
    new_file.write(result_str)
    new_file.close()
    data_file.close()

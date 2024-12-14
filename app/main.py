def create_report(data_file_name: str, report_file_name: str) -> None:
    fl = open(data_file_name)
    result_list = fl.readlines()
    buy_ls = []
    supply_ls = []
    for value in result_list:
        value = value.strip()
        if value.startswith("buy"):
            buy_ls.append(int(value[4:]))
        else:
            supply_ls.append(int(value[7:]))

    total_buy = sum(buy_ls)
    total_supply = sum(supply_ls)
    result = total_supply - total_buy

    fl.close()

    fl = open(report_file_name, "w")

    fl.write(f"supply,{total_supply}\n")
    fl.write(f"buy,{total_buy}\n")
    fl.write(f"result,{result}\n")

    fl.close()

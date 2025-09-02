def create_report(data_file_name: str, report_file_name: str) -> None:
    file_r = open(f"./{data_file_name}", "r")

    supply_list_values = []
    buy_list_values = []

    for line in file_r:
        line_info = line.split(",")

        if line_info[0] == "supply":
            supply_list_values.append(int(line_info[1]))
        elif line_info[0] == "buy":
            buy_list_values.append(int(line_info[1]))

    file_r.close()

    supply_sum = sum(supply_list_values)
    buy_sum = sum(buy_list_values)
    total = supply_sum - buy_sum

    file_w = open(f"./{report_file_name}", "w")
    file_w.write(f"supply,{supply_sum}")
    file_w.write(f"\nbuy,{buy_sum}")
    file_w.write(f"\nresult,{total}\n")
    file_w.close()

def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_sum = 0
    buy_sum = 0

    with open(data_file_name, "r") as file, \
            open(report_file_name, "w") as result:
        new_list = file.read().replace("\n", " ").split()
        for list_str in new_list:
            if list_str[0] == "s":
                supply_sum += int(list_str[7:])
            else:
                buy_sum += int(list_str[4:])
        res = supply_sum - buy_sum
        result.write(f"supply,{supply_sum}\nbuy,{buy_sum}\nresult,{res}\n")

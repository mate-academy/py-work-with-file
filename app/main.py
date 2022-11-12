def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_list = []
    buy_list = []
    with open(f"{data_file_name}", "r") as file_in:
        for line in file_in:
            if line.split(",")[0] == "supply":
                supply_list.append(int(line.split(",")[1]))
            if line.split(",")[0] == "buy":
                buy_list.append(int(line.split(",")[1]))
            if line is None:
                return None
    supply_sum = sum(supply_list)
    buy_sum = sum(buy_list)
    result = supply_sum - buy_sum
    with open(f"{report_file_name}", "w") as file_out:
        file_out.write(f"supply,{supply_sum}\nbuy,{buy_sum}\nresult,{result}")

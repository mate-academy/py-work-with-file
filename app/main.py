def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name) as data_file:
        data_list = []
        for data in data_file:
            data = data.strip()
            data = data.split(",")
            data_list.append(data)

        supply_value = []
        buy_value = []
        for lines in data_list:
            if lines[0] == "supply":
                supply_value.append(int(lines[1]))
            if lines[0] == "buy":
                buy_value.append(int(lines[1]))

    with open(report_file_name, "w") as file:
        file.write(
            f"supply,{sum(supply_value)}\n"
            f"buy,{sum(buy_value)}\n"
            f"result,{sum(supply_value) - sum(buy_value)}\n"
        )

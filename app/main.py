from csv import reader


def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as source_file:
        new_data = reader(source_file)
        source_data = list(new_data)
        supply_sum = 0
        buy_sum = 0
        for i in range(len(source_data)):
            if source_data[i][0] == "supply":
                supply_sum += int(source_data[i][1])
            if source_data[i][0] == "buy":
                buy_sum += int(source_data[i][1])
        result = supply_sum - buy_sum
    with open(report_file_name, "w") as input_file:
        input_file.write(f"supply,{supply_sum}\n"
                         f"buy,{buy_sum}\nresult,{result}\n")

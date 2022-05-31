def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, "r") as file_1:
        supply_count = 0
        buy_count = 0

        for line in file_1:
            line = line.split(",")
            if line[0] == "supply":
                supply_count += int(line[1])
            elif line[0] == "buy":
                buy_count += int(line[1])
        result = supply_count - buy_count

    with open(report_file_name, "w") as file_2:
        file_2.write(f"supply,{supply_count}\n")
        file_2.write(f"buy,{buy_count}\n")
        file_2.write(f"result,{result}\n")

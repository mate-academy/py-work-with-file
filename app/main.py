def create_report(data_file_name: str, report_file_name: str) -> None:
    supply_data = 0
    buy_data = 0
    with open(data_file_name, "r") as file:
        for line in file:
            line = line.split(",")
            if line[0] == "supply":
                supply_data += int(line[1])
            else:
                buy_data += int(line[1])
    with open(report_file_name, "w") as new_file:
        new_file.write(f"supply,{supply_data}\n")
        new_file.write(f"buy,{buy_data}\n")
        new_file.write(f"result,{supply_data - buy_data}\n")

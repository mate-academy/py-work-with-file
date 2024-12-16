def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file:
        supply_count = 0
        buy_count = 0
        for line in file.readlines():
            line = line.replace("\n", " ").split(",")
            if line[0] == "supply":
                supply_count += int(line[1])
            if line[0] == "buy":
                buy_count += int(line[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply_count}\n"
                   f"buy,{buy_count}\n"
                   f"result,{supply_count - buy_count}\n")

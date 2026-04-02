def create_report(data_file_name: str, report_file_name: str):
    with open(data_file_name, 'r') as f:
        supply_count, buy_count = 0, 0
        for line in f:
            line = line.split(",")
            if line[0] == "supply":
                supply_count += int(line[1])
            elif line[0] == "buy":
                buy_count += int(line[1])

    with open(report_file_name, "w") as f:
        f.write(f"supply,{supply_count}\n"
                f"buy,{buy_count}\n"
                f"result,{supply_count - buy_count}\n")

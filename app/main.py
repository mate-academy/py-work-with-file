def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file1:
        apples = file1.readlines()
        supply_sum = 0
        buy_sum = 0
        result = 0
        for line in apples:
            parts = line.split(",")
            if parts[0] == "buy":
                buy_sum += int(parts[1])
            elif parts[0] == "supply":
                supply_sum += int(parts[1])
        result = supply_sum - buy_sum
    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{supply_sum}\n")
        file2.write(f"buy,{buy_sum}\n")
        file2.write(f"result,{result}\n")

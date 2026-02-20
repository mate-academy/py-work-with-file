def create_report(data_file_name: str, report_file_name: str) -> None:
    all_supply = 0
    all_buy = 0
    with open(data_file_name, "r") as file1:
        for line in file1:
            line.strip()
            operation, value = line.split(",")
            if operation == "supply":
                all_supply += int(value)
            elif operation == "buy":
                all_buy += int(value)
    result = all_supply - all_buy
    with open(report_file_name, "w") as file2:
        file2.write(f"supply,{all_supply}\n")
        file2.write(f"buy,{all_buy}\n")
        file2.write(f"result,{result}\n")
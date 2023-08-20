def create_report(data_file_name: str, report_file_name: str) -> None:
    new_supply = 0
    new_buy = 0
    with open(data_file_name, "r") as f:
        lines = f.readlines()
        for line in lines:
            value = line.split(",")
            if value[0] == "supply":
                new_supply += int(value[1])
            if value[0] == "buy":
                new_buy += int(value[1])
        result = new_supply - new_buy
    with open(report_file_name, "w") as f:
        f.write(f"supply,{new_supply}\n")
        f.write(f"supply,{new_buy}\n")
        f.write(f"supply,{result}\n")

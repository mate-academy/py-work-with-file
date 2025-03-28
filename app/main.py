def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        total_supply = 0
        total_buy = 0
        for line in data_file.readlines():
            if line.split(",")[0] == "supply":
                total_supply += int(line.split(",")[1])
            if line.split(",")[0] == "buy":
                total_buy += int(line.split(",")[1])

        result = total_supply - total_buy
    with open(report_file_name, "a") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

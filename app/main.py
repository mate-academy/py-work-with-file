def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data, \
            open(report_file_name, "w") as report:
        total_supply = 0
        total_buy = 0
        for line in data:
            if line.split(",")[0] == "buy":
                total_buy += int(line.split(",")[1])
            if line.split(",")[0] == "supply":
                total_supply += int(line.split(",")[1])
        result = total_supply - total_buy
        report.write(f"supply,{total_supply}\n"
                     f"buy,{total_buy}\n"
                     f"result,{result}\n")

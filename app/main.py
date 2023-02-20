def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file,\
            open(report_file_name, "w") as report_file:
        total_supply = 0
        total_buy = 0
        for line in data_file:
            print(line)
            action, amount = line.split(",")
            if action == "supply":
                total_supply += int(amount)
            if action == "buy":
                total_buy += int(amount)
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{total_supply - total_buy}\n")

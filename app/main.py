def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_in,\
            open(report_file_name, "w") as file_out:
        total_supply = 0
        total_buy = 0
        for line in file_in:
            print(line)
            operation, amount = line.split(",")
            if operation == "supply":
                total_supply += int(amount)
            if operation == "buy":
                total_buy += int(amount)
        file_out.write(f"supply,{total_supply}\n")
        file_out.write(f"buy,{total_buy}\n")
        file_out.write(f"result,{total_supply - total_buy}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:

    save_supply = 0
    save_buy = 0
    with open(data_file_name) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            line = line.split(",")
            operation, amount = line
            if operation == "supply":
                save_supply += int(amount)
            else:
                save_buy += int(amount)
    result = save_supply - save_buy
    with open(report_file_name, "w") as file:
        file.write(f"supply,{save_supply}\n")
        file.write(f"buy,{save_buy}\n")
        file.write(f"result,{result}\n")

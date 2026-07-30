def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        for line in file:
            data = line.strip().split(",")

            if data[0] == "supply":
                total_supply += int(data[1])
            else:
                total_buy += int(data[1])

    with open(report_file_name, "w") as file:
        file.write(f"supply,{total_supply}\n"
                   f"buy,{total_buy}\n"
                   f"result,{total_supply - total_buy}\n")

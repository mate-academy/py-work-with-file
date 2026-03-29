def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    with open(data_file_name, "r") as file:
        line = file.readline().strip("\n")
        while line:
            parts = line.split(",")
            if parts[0] == "supply":
                total_supply += int(parts[1])
            elif parts[0] == "buy":
                total_buy += int(parts[1])

            line = file.readline().strip("\n")

    result = total_supply - total_buy

    with open(report_file_name, "a") as report_file:
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as first_file:
        first_information = first_file.read()
        total_supply = 0
        total_buy = 0
        information = first_information.split("\n")
        for line in information:
            if line.split(",")[0] == "supply":
                total_supply += int(line.split(",")[1])
            elif line.split(",")[0] == "buy":
                total_buy += int(line.split(",")[1])

    with open(report_file_name, "a") as report_file:
        result = total_supply - total_buy
        report_file.write(f"supply,{total_supply}\n")
        report_file.write(f"buy,{total_buy}\n")
        report_file.write(f"result,{result}")

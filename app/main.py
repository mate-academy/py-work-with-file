def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    data_file = open(data_file_name, "r")

    for line in data_file:
        line = line.strip()

        if line:
            line = line.split(",")

            if line[0] == "supply":
                total_supply += int(line[1])
            elif line[0] == "buy":
                total_buy += int(line[1])

    data_file.close()

    result = total_supply - total_buy

    report_file = open(report_file_name, "w")
    report_file.write(f"supply,{total_supply}\n")
    report_file.write(f"buy,{total_buy}\n")
    report_file.write(f"result,{result}\n")

    report_file.close()

def create_report(data_file_name: str, report_file_name: str) -> None:
    total_supply = 0
    total_buy = 0

    data_file = open(data_file_name, "r")

    for data in data_file:
        data = data.strip()

        if data:
            data = data.split(",")

        if data[0] == "supply":
            total_supply += int(data[1])
        elif data[0] == "buy":
            total_buy += int(data[1])

    data_file.close()

    result = total_supply - total_buy

    with open(report_file_name, "w") as file:
        file.write(f"supply, {total_supply}\n")
        file.write(f"buy, {total_buy}\n")
        file.write(f"result, {result}\n")

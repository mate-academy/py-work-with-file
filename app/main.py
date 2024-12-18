def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as input:
        input_data = input.read()
        total_supply = 0
        total_buy = 0
        for line in input_data:
            if line == "":
                continue
            if line[0] == "supply":
                total_supply += line[1]
            elif line[0] == "buy":
                total_buy += line[1]
        result = total_supply - total_buy
    with open(report_file_name, "w") as output:
        output.write(f"supply, {total_supply}")
        output.write(f"buy, {total_buy}")
        output.write(f"result, {result}")

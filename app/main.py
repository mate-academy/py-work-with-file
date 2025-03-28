def create_report(data_file_name: str, report_file_name: str = None) -> None:
    sum_supply = 0
    sum_buy = 0
    with open(data_file_name, "r") as firstfile:
        for line in firstfile:
            line_split = line.strip().split(",")
            if "supply" in line_split:
                sum_supply += int(line_split[1])
            elif "buy" in line_split:
                sum_buy += int(line_split[1])
            else:
                continue

        result = sum_supply - sum_buy

        with open(report_file_name, "a") as secondfile:
            secondfile.write("supply," + str(sum_supply) + "\n")
            secondfile.write("buy," + str(sum_buy) + "\n")
            secondfile.write("result," + str(result) + "\n")

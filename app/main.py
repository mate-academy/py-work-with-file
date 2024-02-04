def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r", newline="") as csv_file:

        total_supply = 0
        total_buy = 0

        for line in csv_file:
            line_list = line.replace(",", " ").strip().split()
            if line_list[0] == "supply":
                total_supply += int(line_list[1])
            if line_list[0] == "buy":
                total_buy += int(line_list[1])

        result = total_supply - total_buy

        with open(report_file_name, "w") as report_file:
            report_file.write(f"supply,{total_supply}\n"
                              f"buy,{total_buy}\n"
                              f"result,{result}\n")

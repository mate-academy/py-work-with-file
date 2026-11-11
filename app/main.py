def create_report(data_file_name: str, report_file_name: str) -> None:
    with (
        open(data_file_name, "r") as data_file,
        open(report_file_name, "w") as report_file
    ):
        total_supply = 0
        total_buy = 0
        for line in data_file:
            splitted_line = line.split(",")
            if splitted_line[0] == "supply":
                total_supply += int(splitted_line[1])
            else:
                total_buy += int(splitted_line[1])

        report_file.write(
            f"supply,{total_supply}\n"
            f"buy,{total_buy}\n"
            f"result,{total_supply - total_buy}\n"
        )

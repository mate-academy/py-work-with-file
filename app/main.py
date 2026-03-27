def create_report(data_file_name: str,
                  report_file_name: str) -> None:
    with (open(data_file_name, "r") as source,
          open(report_file_name, "w") as report):
        total_supply = 0
        total_buy = 0
        for line in source.readlines():
            line = line.split(",")
            if line[0] == "supply":
                total_supply += int(line[1])
            elif line[0] == "buy":
                total_buy += int(line[1])
        result = total_supply - total_buy
        report.write(f"supply,{total_supply}\n"
                     f"buy,{total_buy}\n"
                     f"result,{result}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as data_file,
          open(report_file_name, "w") as report_file):
        supply = 0
        buy = 0
        for line in data_file.readlines():
            if line.startswith("supply"):
                supply += int(line.split(",")[1])
            elif line.startswith("buy"):
                buy += int(line.split(",")[1])
        result = supply - buy
        supply_str = "supply,"
        buy_str = "buy,"
        result_str = "result,"
        report_file.write(
            f"{supply_str}{supply}\n"
            f"{buy_str}{buy}\n"
            f"{result_str}{result}\n"
        )

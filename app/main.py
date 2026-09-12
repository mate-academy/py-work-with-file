def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if "supply" in line:
                supply_str = line[7:]
                supply_int = int(supply_str)
                supply += supply_int
            if "buy" in line:
                buy_str = line[4:]
                buy_int = int(buy_str)
                buy += buy_int
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        result = supply - buy
        report_file.write(f"result,{result}\n")

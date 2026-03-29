def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file:
        supply = 0
        buy = 0
        for row in data_file:
            name_type, amount = row.split(",")
            if name_type == "supply":
                supply += int(amount)
            elif name_type == "buy":
                buy += int(amount)
        result = supply - buy
    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{result}\n")

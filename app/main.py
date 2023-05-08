def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file, open(report_file_name, "a") as report_file:
        supply = 0
        buy = 0
        for line in data_file.readlines():
            action, quantity = line.split(",")
            if action == "supply":
                supply += int(quantity)
            if action == "buy":
                buy += int(quantity)
        report_file.write(f"supply,{supply}\n")
        report_file.write(f"buy,{buy}\n")
        report_file.write(f"result,{supply - buy}\n")

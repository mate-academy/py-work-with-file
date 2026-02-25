def create_report(data_file_name: str, report_file_name: str) -> None:
    buy_var = 0
    supply_var = 0
    with open(data_file_name, "r") as data_file:
        for line in data_file:
            if "buy" in line:
                buy_var += int(line[4:])

            if "supply" in line:
                supply_var += int(line[7:])

    with open(report_file_name, "w") as report_file:
        report_file.write(f"supply,{supply_var}\n")
        report_file.write(f"buy,{buy_var}\n")
        report_file.write(f"result,{supply_var - buy_var}\n")

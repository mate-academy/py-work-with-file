def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as data_file,\
         open(report_file_name, "a") as report:
        data_list = data_file.readlines()
        supply_count = 0
        buy_count = 0
        for i in data_list:
            if "supply" in i:
                supply_count += int(i.split(",")[1])
            if "buy" in i:
                buy_count += int(i.split(",")[1])
        report.write(f"supply,{supply_count}\n")
        report.write(f"buy,{buy_count}\n")
        report.write(f"result,{supply_count - buy_count}\n")

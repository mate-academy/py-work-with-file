def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_data,\
            open(report_file_name, "w") as file_report:
        supply = 0
        buy = 0
        for line in file_data:
            if "supply" in line:
                supply += int(line.split(",")[1])
            if "buy" in line:
                buy += int(line.split(",")[1])
        file_report.write(f"supply,{supply}\n"
                          f"buy,{buy}\n"
                          f"result,{supply - buy}"
                          f"\n")

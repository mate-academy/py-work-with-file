def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file,\
            open(report_file_name, "a") as report_file:
        for line in file:
            line_list = line.split(",")
            if line_list[0] == "supply":
                supply += int(line_list[1])
            elif line_list[0] == "buy":
                buy += int(line_list[1])
        report_file.write(f"supply,{str(supply)}\n")
        report_file.write(f"buy,{str(buy)}\n")
        report_file.write(f"result,{str(supply - buy)}\n")

def create_report(data_file_name: str, report_file_name: str) -> None:
    with (open(data_file_name, "r") as file_in,
          open(report_file_name, "a") as file_out):
        supply_count = 0
        buy_count = 0
        for line in file_in:
            splitline = line.split(",")
            if splitline[0] == "supply":
                supply_count += int(splitline[1])
            else:
                buy_count += int(splitline[1])
        result = supply_count - buy_count
        file_out.write(f"supply,{supply_count}\n")
        file_out.write(f"buy,{buy_count}\n")
        file_out.write(f"result,{result}\n")

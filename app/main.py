def create_report(data_file_name: str, report_file_name: str) -> None:
    with open(data_file_name, "r") as file_out,\
            open(report_file_name, "w") as file_in:
        buy = 0
        supply = 0
        for line in file_out:
            split_line = line.split(",")
            if split_line[0] == "buy":
                buy += int(split_line[1])
            if split_line[0] == "supply":
                supply += int(split_line[1])
        result = supply - buy
        file_in.write(f"supply,{supply}\n"
                      f"buy,{buy}\n"
                      f"result,{result}\n")

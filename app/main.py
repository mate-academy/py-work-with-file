def create_report(data_file_name: str, report_file_name: str) -> str:
    with open(data_file_name, "r") as file_read:
        supply = 0
        buy = 0
        for line in file_read:
            split_line = line.split(",")
            if split_line[0] == "buy":
                buy += int(split_line[1])
            if split_line[0] == "supply":
                supply += int(split_line[1])
        result = supply - buy
        with open(report_file_name, "w") as file_write:
            file_write.write(f"supply,{supply}\n")
            file_write.write(f"buy,{buy}\n")
            file_write.write(f"result,{result}\n")

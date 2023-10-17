def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0
    with open(data_file_name, "r") as file:
        for line in file.readlines():
            split_line = line.split(",")
            if split_line[0] == "supply":
                supply += int(split_line[1])
            if split_line[0] == "buy":
                buy += int(split_line[1])
    result = supply - buy
    with open(report_file_name, "w") as file:
        file.write(f"supply,{supply}\n"
                   f"buy,{buy}\n"
                   f"result,{result}\n")

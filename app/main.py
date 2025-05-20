def create_report(data_file_name: str, report_file_name: str) -> None:
    supply = 0
    buy = 0

    with open(data_file_name, "r") as file_open:
        for line in file_open:
            line = line.strip()
            if not line:
                continue
            split_str = line.split(",")
            if split_str[0] == "supply":
                supply += int(split_str[1])
            elif split_str[0] == "buy":
                buy += int(split_str[1])

    result = supply - buy

    with open(report_file_name, "w") as file_write:
        file_write.write(f"supply,{supply}\n")
        file_write.write(f"buy,{buy}\n")
        file_write.write(f"result,{result}\n")

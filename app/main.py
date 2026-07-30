def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name, "r")
    write_file = open(report_file_name, "w")
    supply, buy = 0, 0

    for line in read_file:
        split_line = line.split(",")
        if "supply" in split_line:
            supply += int(split_line[1])
        elif "buy" in split_line:
            buy += int(split_line[1])

    read_file.close()

    result = supply - buy

    write_file.write(f"supply,{supply}\n")
    write_file.write(f"buy,{buy}\n")
    write_file.write(f"result,{result}\n")

    write_file.close()

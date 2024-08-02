def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read_from = open(data_file_name, "r")
    file_to_write_in = open(report_file_name, "w")

    supply = 0
    buy = 0
    for line in file_to_read_from:
        if line.startswith("supply"):
            supply += int(line[line.find(",") + 1:])
        elif line.startswith("buy"):
            buy += int(line[line.find(",") + 1:])

    file_to_read_from.close()

    file_to_write_in.write(f"supply,{supply}\n"
                           f"buy,{buy}\n"
                           f"result,{supply - buy}\n")

    file_to_write_in.close()

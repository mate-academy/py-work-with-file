def create_report(data_file_name: str, report_file_name: str) -> None:
    read_file = open(data_file_name)
    supply = 0
    buy = 0
    for line in read_file:
        if line[0:6] == "supply":
            supply += int(line[7:-1])
        if line[0:3] == "buy":
            buy += int(line[4:-1])
    read_file.close()
    print(supply, buy)
    write_file = open(report_file_name, "w")
    write_file.write(f"supply,{supply}\n")
    write_file.write(f"buy,{buy}\n")
    write_file.write(f"result,{supply - buy}\n")
    write_file.close()

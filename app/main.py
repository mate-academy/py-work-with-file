def create_report(data_file_name: str, report_file_name: str) -> None:
    file_to_read = open(data_file_name)
    supply = 0
    buy = 0
    for line in file_to_read:
        if line:
            splitted = line.split(",")
            if splitted[0] == "supply":
                supply += int(splitted[1])
            else:
                buy += int(splitted[1])
    result = supply - buy
    file_to_read.close()
    file_to_write = open(report_file_name, "w")
    file_to_write.write(
        "supply" + "," + str(supply) + "\n"
        + "buy" + "," + str(buy) + "\n"
        + "result" + "," + str(result) + "\n"
    )
    file_to_write.close()

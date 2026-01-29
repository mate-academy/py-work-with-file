def create_report(data_file_name: str, report_file_name: str) -> None:
    # data_file_name
    supply = 0
    buy = 0
    read_file = open(data_file_name, "r")
    for line in read_file.readlines():
        product_info = line.split(",")
        if product_info[0] == "buy":
            buy += int(product_info[1])
        elif product_info[0] == "supply":
            supply += int(product_info[1])

    result = supply - buy
    read_file.close()

    # report_file_name
    write_file = open(report_file_name, "w")
    write_file.write("supply," + str(supply) + "\n")
    write_file.write("buy," + str(buy) + "\n")
    write_file.write("result," + str(result) + "\n")
    write_file.close()

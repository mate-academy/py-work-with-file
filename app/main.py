def create_report(data_file_name: str, report_file_name: str):
    file1 = open(data_file_name, "rt")
    supply = 0
    buy = 0
    for file in file1:
        if "supply" in file:
            supply += int(file.split(",")[-1])
        if "buy" in file:
            buy += int(file.split(",")[-1])
    result = supply - buy
    file1.close()
    file2 = open(report_file_name, "w")
    file2.write("supply" + "," + str(supply) + "\n")
    file2.write("buy," + str(buy) + "\n")
    file2.write("result," + str(result) + "\n")
    file2.close()
